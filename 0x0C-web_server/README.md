# 0x0C. Web server

#### 0\. Transfer a file to your server

Write a Bash script that transfers a file from our client to a server:

Requirements:

-   Accepts 4 parameters
    1.  The path to the file to be transferred
    2.  The IP of the server we want to transfer the file to
    3.  The username `scp` connects with
    4.  The path to the SSH private key that `scp` uses
-   Display `Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY` if less than 3 parameters passed
-   `scp` must transfer the file to the user home directory `~/`
-   Strict host key checking must be disabled when using `scp`

#### 1\. Install nginx web server

Web servers are the piece of software generating and serving HTML pages, let's install one!

Requirements:

-   Install `nginx` on your `web-01` server
-   Nginx should be listening on port 80
-   When querying Nginx at its root `/` with a GET request (requesting a page) using `curl`, it must return a page that contains the string `Holberton School`
-   As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements

#### 2\. Setup a domain name

[.TECH Domains](https://intranet.hbtn.io/rltoken/yRrwiHrS15iQQZku72p0aQ ".TECH Domains") is one of the top domain providers. They are known for the stability and quality of their DNS hosting solution. Holberton School partnered with .TECH Domains so that you can learn about DNS.

.TECH Domains worked with domain name registrars to give you access to a free domain name for a year. Please get the promo code in your [tools space](https://intranet.hbtn.io/rltoken/F0ZPUs7ODLLwp8lr-um8Xg "tools space"). Feel free to drop a thank you tweet for [.TECH Domains](https://intranet.hbtn.io/rltoken/d9XjYlM-CqTRHJEcaKpcVQ ".TECH Domains").

Provide the domain name in your answer file.

Requirement:

-   provide the domain name only (example: `foobar.tech`), no subdomain (example: `www.foobar.tech`)
-   configure your DNS records with an A entry so that your root domain points to your `web-01` IP address **Warning: the propagation of your records can take time (~1-2 hours)**
-   go to [your profile](https://intranet.hbtn.io/rltoken/fYvJr4-HV1WPnfB7HCue_Q "your profile") and enter your domain in the `Project website url` field

#### 3\. Redirection mandatory

Readme:

-   [Replace a line with multiple lines with sed](https://intranet.hbtn.io/rltoken/Afg1zCifjmIygL1se0ghhg "Replace a line with multiple lines with sed")

Configure your Nginx server so that `/redirect_me` is redirecting to another page.

Requirements:

-   The redirection must be a "301 Moved Permanently"
-   You answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements
-   Using what you did with `1-install_nginx_web_server`, write `3-redirection` so that it configures a brand new Ubuntu machine to the requirements asked in this task

#### 4\. Not found page 404 mandatory

Configure your Nginx server to have a custom 404 page that contains the string `Ceci n'est pas une page`.

Requirements:

-   The page must return an HTTP 404 error code
-   The page must contain the string `Ceci n'est pas une page`
-   Using what you did with `3-redirection`, write `4-not_found_page_404` so that it configures a brand new Ubuntu machine to the requirements asked in this task