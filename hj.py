from github import Github
#import cv2
g = Github("Himanshu-Cyber-Code","Himanshu-Cyber-Code-GitHub-Pass")
repo = g.get_repo("Himanshu-Cyber-Code/test")
while True:
    contents = repo.get_contents("image.png")
    open("image2.png","wb").write(contents.decoded_content)
    #cv2.imshow("client",cv2.imread("image2.png"))
          


