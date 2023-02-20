docker build .

docker-compose up -d

http://localhost/facebook  

#TEST
docker exec -it scrap_facebook-app-1 bash 
pytest test.py::test_read_main  -r a --tb=line > test-results.txt
cat test-results.txt
docker cp scrap_facebook-app-1:/app/test-results.txt .