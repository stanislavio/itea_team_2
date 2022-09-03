#https://docs.djangoproject.com/en/4.1/howto/custom-management-commands/
from django.core.management.base import BaseCommand
from db.models import User

import pydenticon
import hashlib
import random
import os

GEN_USERS_MEDIA_FOLDER = r'C:\Users\Vasilyev\AGVDocs\Dev\2. Python\23. Django\4. ActualITEADjangoProject\media'

#https://github.com/azaghal/pydenticon/blob/master/docs/usage.rst
def generateDenticon(str2Hash, path2Save=""):
    foreground = [ "rgb(45,79,255)",
               "rgb(254,180,44)",
               "rgb(226,121,234)",
               "rgb(30,179,253)",
               "rgb(232,77,65)",
               "rgb(49,203,115)",
               "rgb(141,69,170)" ]

    
    background = "rgb(227,242,253)"#e3f2fd

    generator = pydenticon.Generator(
                    10, 10,
                    foreground=foreground, background=background
                )
    denticon = generator.generate(
                    str2Hash, 100, 100,
                    inverted=True, output_format="png"
                )

    img_name = 'gen_users'+os.sep+path2Save+'.png'
    img_path = GEN_USERS_MEDIA_FOLDER+os.sep+img_name
    print("Image saved to path", img_path)
    f = open(img_path, "wb")
    f.write(denticon)
    f.close()
    return img_name

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    


    def handle(self, *args, **options):
        print("Working handle")
        number_of_users = User.objects.all().count()
        print('There are users:', number_of_users)

        NEEDED_USERS = 10

        #Names list
        f = open('frontend\management\commands\human_names_03Sep2022.txt', 'r')
        name_list = f.readlines()
        f.close()

        #Short_bio list
        f=open('frontend\management\commands\maximes_03Sep2022_no_new_lines.txt', 'r', encoding='utf-8')
        maximes_list = f.readlines()
        f.close()


        for usr in User.objects.all():
            print("have user:", usr.username)
            print('Bio:', usr.short_bio)
            if(len(usr.short_bio) == 0):
                usr.short_bio = random.choice(maximes_list).strip()
                print('Will add new bio:', usr.short_bio)
                usr.save()




        # for i in range(NEEDED_USERS-number_of_users):
        for i in range(1):
            print("Creating user")
            rnd_name = random.choice(name_list)
            fName, lName = rnd_name.split(' ')
            lName = lName.rstrip()
            #TODO add UUID part to generated user names
            usr_name = f"{fName}_{lName}_{random.randint(1, 999)}_g"

            img_name = generateDenticon(usr_name, usr_name)

            new_user = User(
                username = usr_name,
                first_name = fName,
                last_name = lName,
                email = f"{fName}{lName}@server.com",
                photo = img_name,
                short_bio = random.choice(maximes_list).strip()
            )
            new_user.save()

            new_user.set_password('qwe1')
            new_user.save()

            

        


        # self._create_tags()