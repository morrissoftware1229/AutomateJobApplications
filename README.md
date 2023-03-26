
# Project Outline

1. Accept user input including search string, location string, resume path, and remote binary  
2. Navigate to Indeed.com  
3. Enter information from user  
4. Selects first available option  
5. Displays job description and asks user if they want to apply (if user selects no, repeat with next job)  
6. If user selects yes, check for easy apply or external apply  
7. Check value of box  
8. If value has automated answer, enter answer; else, prompt user for input  
9. Submit application  
10. Repeat from line 4  

# Issues Encountered  

1. Sometimes elements can't be found if you don't include wait time  
2. Indeed may be performing A-B testing with remote option, so multiple scenarios had to be included  
3. Dropdown options weren't selectable by id, so I had to use action chains  
4. Text from location box needed to be cleared out with send_keys. Previously, my input was concatenated with default value  
5. Needed to capture keyboard input. Pulled a script from Stack Overflow, but needed to learn about the Win32API, Windows naming conventions, and C++ naming conventions.