
import instaloader

instafun = instaloader.Instaloader()

inputname = input("Enter ig profile name : ")

instafun.download_profile( inputname, profile_pic_only = True)

