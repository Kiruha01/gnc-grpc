# gRPC task
## Description
Using grpc, create an API to query a database/storage of your choice 
(SQL, Redis, etc.). API should have the following methods:
* get item by id
* put item
* delete item by id
* get many items (with paging - you provide a page number and page length)

The API code should be generated from a proto file, you should be 
able to demonstrate querying this API from another application.

Implementation in **Python**.

## Files

* `client/` - folder with client code
  * `grpc_module` - files generated from *.proto* file
  * `main.py` - script to run client
  * `requirements.txt` - list of dependencies
* `server/` - folder with server code
  * `db` - folder with description db
  * `grpc_module` - files generated from *.proto* file
  * `main.py` - script to run sever
  * `requirements.txt` - list of dependencies
* `docker-compose.yml` - file to run server
* `items.proto` - proto file for gRPC

## Reproducible steps
### Run server
To run server type
```shell
docker-compose up
```
That command run server on port `50051`

### Run client
1. To run client move to `client` folder
    ```shell
    cd client/
    ```
2. Create and activate python virtual environment
    ```shell
    python -m venv venv
    source venv/bin/activate
    ```
3. Install dependencies
    ```shell
    pip install -r requirements.txt
    ```
4. Run client
    ```shell
    python main.py
    ```

### Manipulate with client
You can manipulate items in the client CLI with commands.
Type `\h` for help message.

```
Items client. Type \h for help.
>> \h

Commands:
* \h - help
* \q - quit

* \c - create item
* \d - delete item
* \g - get item
* \gs - get many items

>>
```