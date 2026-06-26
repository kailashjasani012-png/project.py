def create_file(fname):
    f = open(fname, "w")
    f.close()
    return "File created successfully!"

def write_file(fname, data):
    f = open(fname, "w")
    f.write(data)
    f.close()
    return "Data written successfully!"

def read_file(fname):
    try:
        f = open(fname, "r")
        data = f.read()
        f.close()
        return data
    except:
        return "File does not exist."

def append_file(fname, data):
    f = open(fname, "a")
    f.write(data)
    f.close()
    return "Data appended successfully!"