# Portfolio
- Hello
- It's me
- I've been wondering
- If you want to visit my portfolio
- [Hamdallah Fatayer](http://54.227.22.228//)
- [Resume](https://drive.google.com/file/d/1QhxyIwPO_ka_cgSjsZpjUd3bRYrobIJH/view?usp=sharing)

[![pic](https://i.imgur.com/nqobfru.png)](http://3.135.20.94/)

## New code lines used
- ```docker ps```
- ```docker build . -t imagename```
- ```docker tag imagename user/imagename```
- ```docker push user/imagename```
- ```docker kill containername```

- gitbash change key permissions
- ```chmod 400 keyname.pem```
- gitbash copy all files to vm
- ```scp -r -i keyname.pem ./path/to/docker-compose ec2-user@publicIP:~/```
- gitbash enter vm
- ```ssh -i keyname.pem ec2-user@publicDNS```
- ubuntu install docker
- ```sudo yum install docker```
- ```sudo systemctl start docker```
- ubuntu install docker-compose
- ```sudo curl -L https://github.com/docker/compose/releases/download/1.21.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose```
- ```sudo chmod +x /usr/local/bin/docker-compose```
- ubuntu change env path
- ```sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose```
- ```sudo service docker restart```
- ubuntu run docker
- ```sudo docker run -d -p 8000:80 user/imagename```
- ubuntu run docker compose
- ```sudo docker-compose up --build```
