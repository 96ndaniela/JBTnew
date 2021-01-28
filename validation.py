 #!/usr/bin/env python3
import mimetypes

validation = mimetypes.guess_extension(path)
print(validation)

if(validation !== ".csv"):
    print("this type of file isn't supported") 
