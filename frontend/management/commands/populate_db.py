#https://docs.djangoproject.com/en/4.1/howto/custom-management-commands/
from django.core.management.base import BaseCommand
from db.models import User

import pydenticon
import hashlib
import random
import os

GEN_USERS_MEDIA_FOLDER = r'C:\Users\Vasilyev\AGVDocs\Dev\2. Python\23. Django\4. ActualITEADjangoProject\media'

def generateDenticon(str2Hash, path2Save=""):
    generator = pydenticon.Generator(10, 10)
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

    # def _create_tags(self):
    #     tlisp = Tag(name='Lisp')
    #     tlisp.save()

    #     tjava = Tag(name='Java')
    #     tjava.save()

    


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

        # print(name_list)

        # for i in range(NEEDED_USERS-number_of_users):
        for i in range(1):
            print("Creating user")
            rnd_name = random.choice(name_list)
            fName, lName = rnd_name.split(' ')
            lName = lName.rstrip()
            #TODO add UUID part to generated user names
            usr_name = f"gen_{fName}_{lName}_{random.randint(1, 999)}"

            img_name = generateDenticon(usr_name, usr_name)

            new_user = User(
                username = usr_name,
                first_name = fName,
                last_name = lName,
                email = f"{fName}{lName}@server.com",
                photo = img_name,
                short_bio = random.choice(maximes_list)
            )
            new_user.save()

            new_user.set_password('qwe1')
            new_user.save()

            

        


        # self._create_tags()