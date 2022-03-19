
# ACT Login (Web Scrapping)

This is baically a web scrapper that automates login to `selfcare.actcorp.in` protal. I use `mechanize` to create a browser instance select the `form` and submit it. Additional I monitor the internet reachability using `ping` implementation.

## Deployment
If you have `ACT Fibernet` and you are using Dynamic IP as mode for connection. For this we require a user id and password (contact support if don't have this with you)

1. Create `.env` file in project directory, add the following entries
    
        `UNAME="bunch of numbers"` 
        `pword="user dependent"`

2. Create a python virtual env (preferablly name `scrapping`)

        virtualenv scrapping

3. Install packages using pip (after you enable virtualenv)

        pip install -r requirements.txt

4. Create a soft link from your current directory to /usr/local/lib (This is optional)

       sudo ln -s /home/ubuntu/actlogin/ /usr/local/lib/actlogin 

    (Change the source location based on your case)

5. Copy the `.service` file to `/etc/systemd/system/` for creating service (linking was creating error feel free to try)

        sudo cp actlogin.service /etc/systemd/system/actlogin.service

6. Check if `.service` is detected

        systemctl status actlogin.service

7. Start and enable

        systemctl start actlogin.service 
        systemctl enable actlogin.service

8. (Optional) To monitor the service

        watch journalctl -u actlogin.service -r

## Interesting Things

- Python journalctl is integrated for publishing logs to journalctl
- Script lives on Raspberry Pi, continuously monitoring our network reachability
- To check reachability we ping `8.8.8.8` which is googles public DNS, this is faster and removes DNS resolution
