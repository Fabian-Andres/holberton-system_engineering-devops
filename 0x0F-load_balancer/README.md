# 0x0F. Load balancer

#### 0\. Double the number of webservers

In this first task you need to configure `web-02` to be identical to `web-01`. Fortunately, you built a Bash script during your [web server project](https://intranet.hbtn.io/rltoken/8oRonOh-zV4e2bmsZ3sxEw "web server project"), and they'll now come in handy to easily configure `web-02`. Remember, always try to automate your work!

Since we're placing our web servers behind a load balancer for this project, we want to add a custom Nginx response header. The goal here is to be able to track which web server is answering our HTTP requests, to understand and track the way a load balancer works. More in the coming tasks.

Requirements:

-   Configure Nginx so that its HTTP response contains a custom header (on `web-01` and `web-02`)
    -   The name of the custom HTTP header must be `X-Served-By`
    -   The value of the custom HTTP header must be the hostname of the server Nginx is running on
-   Write `0-custom_http_response-header` so that it configures a brand new Ubuntu machine to the requirements asked in this task
    -   [Ignore](https://intranet.hbtn.io/rltoken/3AOvROMUNUrzxEWhli4GTw "Ignore") [SC2154](https://intranet.hbtn.io/rltoken/i5f8DYX_rRYFz4hfbG_GJg "SC2154") for `shellcheck`


#### 1\. Install your load balancer mandatory

Install and configure HAproxy on your `lb-01` server.

Requirements:

-   Configure HAproxy with version equal or greater than 1.5 so that it send traffic to `web-01` and `web-02`
-   Distribute requests using a roundrobin algorithm
-   Make sure that HAproxy can be managed via an init script
-   Make sure that your servers are configured with the right hostnames: `[STUDENT_ID]-web-01` and `[STUDENT_ID]-web-02`. If not, follow this [tutorial](https://intranet.hbtn.io/rltoken/Tb9qeqRrtrO_b2uFpet9rw "tutorial").
-   For your answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements

#### 2\. Add a custom HTTP header with Puppet #advanced

Just as in task #0, we'd like you to automate the task of creating a custom HTTP header response, but with Puppet.

-   The name of the custom HTTP header must be `X-Served-By`
-   The value of the custom HTTP header must be the hostname of the server Nginx is running on
-   Write `2-puppet_custom_http_response-header.pp` so that it configures a brand new Ubuntu machine to the requirements asked in this task