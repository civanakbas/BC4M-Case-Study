# Instructions For Docker File

Run the commands
```
git clone https://github.com/civanakbas/BC4M-Case-Study.git
docker build --tag bc4m/case:1.0 .
docker run -p 5000:8080 bc4m/case:1.0
```
and open [localhost:5000](http://localhost:5000/) on your browser.
