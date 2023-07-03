
response = 200
import urllib.request as urllib

def main(url):
    print("Checking connectivity  ")
    
    responce = urllib.urlopen(url)
    
    print("Connected to", url, "sucessfully")
    print("The response code was: ", response.getcode())
    
print("This is a site connectivity checker program")
input_url = input("Input he url of the site you want to check: ")

main(input_url)