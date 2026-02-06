class Request:

    def __init__(self, request: bytes):
        
        splitRequest = request.split("\r\n")
        firstSection = splitRequest[0].split(" ")

        self.method = firstSection[0]
        self.path = firstSection[1]
        self.http_version = firstSection[2]

        for i in range(1, len(splitRequest)):
            if splitRequest[i] == "" and splitRequest[i+1] == "":
                break
            else:
                currentLine = splitRequest[i].split(":")
                # the keys of the headers are case-insensitive so this should work
                key = currentLine[0].lower().strip()
                val = currentLine[1].lower().strip()
                self.headers[key] = val

                # for each "header" we add check if its a cookies header so does it exist at all?
                if key == "cookie":
                    # we need to parse this cookie's val. 
                    specialVals = val.split(";")
                    for line in specialVals:
                        l = line.split("=")
                        key = l[0].lower().strip()
                        val = l[1].lower().strip()
                        self.cookies[key] = val


        if self.method == "GET":
            # we are dealing with GET request
            self.body = b""
            pass
        elif self.method == "POST":
            # we are dealing with a POST request
            for i in range(1, len(splitRequest)):
                if splitRequest[i] == "" and splitRequest[i+1] == "":
                    self.body = b'%f{splitRequest[len(splitRequest) - 1]}'
        elif self.method == "PUT":
            # N/A rn
            pass
        elif self.method == "PATCH":
            # N/A rn
            pass
        elif self.method == "DELETE":
            # N/A rn
            pass
        elif self.method == "HEAD":
            # N/A rn
            pass


def test1():
    request = Request(b'GET / HTTP/1.1\r\nHost: localhost:8080\r\nConnection: keep-alive\r\n\r\n')
    assert request.method == "GET"
    assert "Host" in request.headers
    assert request.headers["Host"] == "localhost:8080"  # note: The leading space in the header value must be removed
    assert request.body == b""  # There is no body for this request.
    # When parsing POST requests, the body must be in bytes, not str

    # This is the start of a simple way (ie. no external libraries) to test your code.
    # It's recommended that you complete this test and add others, including at least one
    # test using a POST request. Also, ensure that the types of all values are correct


if __name__ == '__main__':
    test1()
