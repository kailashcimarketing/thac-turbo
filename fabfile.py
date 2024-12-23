import os
import sys
from fabric.colors import yellow, blue, red
from fabric.api import abort, env, cd, prefix, sudo as _sudo, run as _run, \
    hide, task, local
from importlib import import_module

from fabric.context_managers import settings
from fabric.operations import get, put

env.proj_app = "schooldemov6"

conf = {}

# define a dict FABRIC inside settings.py and add project particulars to it. See this example:
# FABRIC = {
#     "DEPLOY_TOOL": "hg",  # Deploy with "git", "hg", or "rsync"
#     "SSH_USER": "",  # VPS SSH username
#     "HOSTS": ['54.213.129.197'],  # The IP address of your VPS
#     "DOMAINS": ALLOWED_HOSTS,  # Edit domains in ALLOWED_HOSTS
#     "REQUIREMENTS_PATH": "requirements.txt",  # Project's pip requirements
#     "LOCALE": "en_US.UTF-8",  # Should end with ".UTF-8"
#     "DB_NAME": 'stadri_db',
#     "DB_PASS": "",  # Live database password
#     "ADMIN_PASS": "",  # Live admin user password
#     "SECRET_KEY": SECRET_KEY,
#     "USER": "user",
#     "KEY_FILE": "~/.ssh/stadrikey.pem",
#     "VENV": "/home/user/Envs/stadri",
#     "CELERY_LOG": '/var/log/celery/celery.log'
# }

if sys.argv[0].split(os.sep)[-1] in ("fab", "fab-script.py"):
    # Ensure we import settings from the current dir
    try:
        conf = import_module("core.settings.base").FABRIC
        try:
            conf["HOSTS"][0]
        except (KeyError, ValueError):
            raise ImportError
    except (ImportError, AttributeError):
        print("Aborting, no hosts defined.")
        exit()

env.hosts = conf["HOSTS"]
env.user = conf["USER"]
env.proj_name = conf.get("PROJECT_NAME", env.proj_app)
env.key_filename = conf.get("PEM_KEY")


@task
def ls_al():
    _run("ls -al")


def virtualenv_command(command):
    source = 'source /home/ec2-user/.virtualenvs/schooldemov6env/bin/activate && '
    sudo(source + command)

@task
def deploy_migrate_restart():
    local("git pull git@github.com:team-and-systems-hq/schooldemov6.git")
    local("pip freeze > requirements.txt; git add .; git commit; git push --verbose --progress git@github.com:team-and-systems-hq/schooldemov6.git")
    sudo("cd /home/ec2-user/webapps/schooldemov6/ && git pull git@github.com:team-and-systems-hq/schooldemov6.git", user="ec2-user")
    virtualenv_command("pip install -r /home/ec2-user/webapps/schooldemov6/requirements.txt")
    virtualenv_command("python /home/ec2-user/webapps/schooldemov6/manage.py migrate")
    virtualenv_command("python /home/ec2-user/webapps/schooldemov6/manage.py collectstatic --noinput")
    sudo("systemctl restart gunicorn-schooldemov6")


@task
def fab_push_html():
    local("git pull; hg update")
    local("git add .; git commit; git push")
    with prefix('source /home/ec2-user/webapps/schooldemov6/bin/activate'):
        _run("cd /home/ec2-user/webapps/schooldemov6; git pull")


def virtualenv(command):
    """
    Run a command in the virtualenv. This prefixes the command with the source
    command.
    Usage:
        virtualenv('pip install django')
    """
    source = 'source %s/bin/activate && ' % conf['VENV']
    _run(source + command)


def _print(output):
    print('\n')
    print(output)
    print('\n')


def print_command(command):
    _print(blue("$ ", bold=True) +
           yellow(command, bold=True) +
           red(" ->", bold=True))


@task
def sudo(command, show=True, *args, **kwargs):
    """
    Runs a command as sudo on the remote server.
    """
    if show:
        print_command(command)
    with hide("running"):
        return _sudo(command, *args, **kwargs)


@task
def run(command, show=True, *args, **kwargs):
    """
    Runs a shell comand on the remote server.
    """
    if show:
        print_command(command)
    with hide("running"):
        return _run(command, *args, **kwargs)


@task
def dump_celery_log():
    _run("tail -1000 %s; date;" % conf['CELERY_LOG'])


@task
def postgres(command):
    """
    Runs the given command as the postgres user.
    """
    show = not command.startswith("psql")
    return sudo(command, show=show, user="postgres")


@task
def backup(filename):
    """
    Backs up the project database.
    """
    tmp_file = "/tmp/%s" % filename
    # We dump to /tmp because user "postgres" can't write to other user folders
    # We cd to / because user "postgres" might not have read permissions
    # elsewhere.
    with cd("/"):
        postgres("pg_dump %s > %s --quote-all-identifiers" % (conf['DB_NAME'], tmp_file))


@task
def local_backup(filename):
    """
    Backs up the local project database to tmp folder.
    """
    tmp_file = "/tmp/%s" % filename
    with settings(sudo_user='postgres'):
        local("/Library/PostgreSQL/9.2/bin/pg_dump --dbname=postgresql://%s:%s@127.0.0.1:5432/%s > %s" %
              (conf['DB_USER'], conf['DB_PASS'], conf['DB_NAME'], tmp_file), shell='/bin/bash')


@task
def file_get(remotepath, localpath):
    get(remotepath, localpath + "." + env.host)


@task
def file_send(localpath, remotepath):
    put(localpath, remotepath, use_sudo=True)


@task
def download_db(filename):
    backup(filename)
    file_get("/tmp/%s" % filename, "/tmp/%s" % filename)


@task
def upload_db(filename):
    local_backup(filename)
    file_send("/tmp/%s" % filename, "/tmp/%s" % filename)


@task
def status_check():
    sudo('sudo supervisorctl status')


@task
def media_backup():
    with prefix('source /home/ec2-user/.virtualenvs/schooldemov6env/bin/activate'):
        _run("python /home/ec2-user/webapps/schooldemov6/manage.py mediabackup")


