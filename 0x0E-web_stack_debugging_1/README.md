# 0x0E. Web stack debugging #1

#### 0\. Nginx likes port 80

Using your debugging skills, find out what's keeping your Ubuntu container's Nginx installation from listening on port `80`. Feel free to install whatever tool you need, start and destroy as many containers as you need to debug the issue. Then, write a Bash script with the minimum number of commands to automate your fix.

#### 1\. Make it sweet and short

Using what you did for task #0, make your fix short and sweet.

Requirements:

-   Your Bash script must be 5 lines long or less
-   There must be a new line at the end of the file
-   You must respect usual Bash script requirements
-   You cannot use `;`
-   You cannot use `&&`
-   You cannot use `wget`
-   You cannot execute your previous answer file (Do not include the name of the previous script in this one)
-   `service` (init) must say that `nginx` is not running ← for real