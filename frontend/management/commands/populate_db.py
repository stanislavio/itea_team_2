#https://docs.djangoproject.com/en/4.1/howto/custom-management-commands/
from django.core.management.base import BaseCommand
from db.models import User, SocialPost

import pydenticon
import hashlib
import random
import os
import datetime

GEN_USERS_MEDIA_FOLDER = r'C:\Users\Vasilyev\AGVDocs\Dev\2. Python\23. Django\4. ActualITEADjangoProject\media'

USER_NAME_FOR_POSTS_AUTHORSHIP = 'vaal12'#TODO: if empty - random user to be selected when post is generated


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
                    7, 7,
                    foreground=foreground, background=background
                )
    denticon = generator.generate(
                    str2Hash, 70, 70,
                    inverted=True, output_format="png"
                )

    img_name = 'gen_users'+os.sep+path2Save+'.png'
    img_path = GEN_USERS_MEDIA_FOLDER+os.sep+img_name
    print("Image saved to path", img_path)
    f = open(img_path, "wb")
    f.write(denticon)
    f.close()
    return img_name

def getRandomDateInThePast(days_at_least = 5000, days_at_most = 15000):
    return datetime.datetime.now()+ \
                datetime.timedelta(
                    days = (-random.randint(days_at_least, days_at_most)) 
                )

def generateUser(name_list, maximes_list):
    print("Creating user")
    rnd_name = random.choice(name_list)
    fName, lName = rnd_name.split(' ')
    lName = lName.rstrip()
    
    #TODO add UUID part to generated user names
    usr_name = f"{fName}_{lName}_{random.randint(1, 999)}_g"
    print("UsrName:", usr_name)

    img_name = generateDenticon(usr_name, usr_name)

    bDay = getRandomDateInThePast()

    new_user = User(
        username = usr_name,
        first_name = fName,
        last_name = lName,
        email = f"{fName}{lName}@server.com",
        photo = img_name,
        short_bio = random.choice(maximes_list).strip(),
        birthday = bDay,
        # phone = '+38044123456'
    )
    new_user.save()

    new_user.set_password('qwe1')
    new_user.save()
#END def generateUser(name_list, maximes_list):

def getBigText(big_text_list, needed_length):
    rnd_start_line = random.randint(0, len(big_text_list))
    big_text = big_text_list[rnd_start_line][:needed_length]
    i=1
    while len(big_text) < needed_length:
        if (rnd_start_line+i) >= len(big_text_list):
            break
        big_text += big_text_list[rnd_start_line+i]
        i+=1
    big_text = big_text[:needed_length]
    return big_text
#END def getBigTex(big_text_list, needed_length):

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
            # print("have user:", usr.username)
            # print('Bio:', usr.short_bio)
            if(len(usr.short_bio) == 0):
                usr.short_bio = random.choice(maximes_list).strip()
                print('Will add new bio:', usr.short_bio)
                usr.save()




        # for i in range(NEEDED_USERS-number_of_users):
        for i in range(1):
            generateUser(name_list, maximes_list)

        gen_post_image_dir = GEN_USERS_MEDIA_FOLDER+os.sep+'gen_posts'+os.sep
        post_img_list = os.listdir(gen_post_image_dir)
        # print(post_img_list)

        # img_path = gen_post_image_dir+\
        img_path =  os.sep+'gen_posts'+os.sep+\
                        post_img_list[
                            random.randint(0, len(post_img_list)-1)
                        ]
        
        print('img_path', img_path)


        big_text_file = open(
            'frontend\management\commands\war_and_peace_03Sep2022.txt', 'r',
            encoding ='utf-8'
            )

        big_text_lines = big_text_file.readlines()

        

        NEEDED_BIG_TEXT_LEN = 2000

        #Update of old posts
        for old_post in SocialPost.objects.all():
            if len(old_post.post_text) < 200:
                old_post.post_text = getBigText(big_text_lines, NEEDED_BIG_TEXT_LEN)
            
            if old_post.author is None:
                author_user = User.objects.filter(
                    username = 'vaal12'
                )[0]
                old_post.author = author_user

            old_post.save()

        #Social POST GENERATION
        for i in range(1):
            print("Generating post")
            author_user = User.objects.filter(
                username = 'vaal12'
            )[0]
            curr_post = SocialPost(
                author = author_user,
                post_title = getBigText(big_text_lines, 120),
                post_text = getBigText(big_text_lines, NEEDED_BIG_TEXT_LEN),
                post_is_private = False,
                post_photo = img_path
            )
            curr_post.save()

    #END