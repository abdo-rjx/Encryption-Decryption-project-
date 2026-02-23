import hashlib

# text = 'hello world!'
# hash_object = hashlib.sha256(text.encode())
# print (hash_object)
# hash_digest = hash_object.hexdigest()
# print (hash_digest)

def hash_file(file_path):
    h = hashlib.new("sha256")
    with open(file_path, "rb") as file:
        while True : 
            chunk = file.read(1024)
            if chunk == b"":
                break
            h.update(chunk)
    return h.hexdigest()

def verify_integrity(file1,file2):
    hash1 = hash_file(file1)
    hash2 = hash_file(file2)
    if hash1 == hash2:
        return "equal"
    else:
        return "not equal" 

if __name__ == "__main__":
    print('the sha code is ', hash_file(r"C:\Users\pc\Desktop\python crypto\venv\sample_files\sample.txt"))
    print(verify_integrity(r"C:\Users\pc\Desktop\python crypto\W20250703_21_08_27_Pro.jpg", r"C:\Users\pc\Desktop\python crypto\WIN_20250703_21_08_27_Pro.jpg"))