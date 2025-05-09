
        document.addEventListener('DOMContentLoaded', function() {
            const bookingsContainer = document.getElementById('bookings-container');
            const addBookingBtn = document.getElementById('add-booking-btn');
            const bookingCountField = document.getElementById('id_booking_count');
            const bookingTemplate = document.getElementById('booking-template').innerHTML;
            
            // Initialize booking count
            let bookingCount = 1;
            
            // Add booking button event listener
            addBookingBtn.addEventListener('click', function() {
                bookingCount++;
                console.log("clicked");
                // Update the hidden field
                bookingCountField.value = bookingCount;
                
                // Create new booking from template
                const newBookingHtml = bookingTemplate.replace(/__INDEX__/g, bookingCount);
                
                // Add the new booking to the container
                const tempDiv = document.createElement('div');
                tempDiv.innerHTML = newBookingHtml;
                const newBooking = tempDiv.firstElementChild;
                bookingsContainer.appendChild(newBooking);
                
                // Initialize the remove button for this booking
                initRemoveButton(newBooking.querySelector('.remove-booking-btn'));
                
                // Update booking numbers
                updateBookingNumbers();
            });
            
            // Initialize remove buttons for existing bookings
            document.querySelectorAll('.remove-booking-btn').forEach(initRemoveButton);
            
            function initRemoveButton(button) {
                button.addEventListener('click', function() {
                    const booking = this.closest('.booking');
                    booking.remove();
                    
                    // Update booking count
                    bookingCount--;
                    bookingCountField.value = bookingCount;
                    
                    // Update booking numbers
                    updateBookingNumbers();
                    
                    // Show all remove buttons if there's more than one booking
                    const removeButtons = document.querySelectorAll('.remove-booking-btn');
                    if (removeButtons.length === 1) {
                        removeButtons[0].style.display = 'none';
                    }
                });
            }
            
            function updateBookingNumbers() {
                // Update all booking numbers in the UI
                document.querySelectorAll('.booking').forEach((booking, index) => {
                    booking.querySelector('.booking-number').textContent = (index + 1);
                    booking.dataset.bookingIndex = (index + 1);
                });
                
                // Show/hide remove buttons based on booking count
                const removeButtons = document.querySelectorAll('.remove-booking-btn');
                if (removeButtons.length === 1) {
                    removeButtons[0].style.display = 'none';
                } else {
                    removeButtons.forEach(btn => btn.style.display = 'inline-flex');
                }
            }
            
            // Set initial booking count
            bookingCountField.value = bookingCount;
        });
    