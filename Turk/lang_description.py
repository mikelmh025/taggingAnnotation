import json
data_dict = {
    'Top_and_front_side': {
        'description':'Please annotation hair on top of the head and bangs',
        'url':'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/100_top.jpg',
        'Length': {
            'description': 'Please annotate the length of top and front side hair. Focus on the absolute hair length, regardless of gender. (Ignore hair on the side of the head for now)',
            'url':'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/110_length.png',
            'option1': {
                'title': 'no hair',
                'description': 'They shaved all the hair on top of head, you can’t see any hair.',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/111_noHair.png',
            },
            'option2': {
                'title': 'High hairline (Bald)',
                'description': 'They have a high hairline, maybe suffers from hair loss.',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/112_highHairLine.png',
            },
            'option3': {
                'title': 'Crew cut',
                'description': 'They have very short hair. Feels like bristly surface of a brush.',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/113_crewCut.png',
            },
            'option4': {
                'title': 'Short Hair',
                'description': 'Natural wind won’t mess up this hair.',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/114_short.png',
            },
            'option5': {
                'title': 'Medium Hair',
                'description': 'Top side hair doesn’t reach his eyebrow.',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/115_medium.png',
            },
            'option6':{
                'title':'Long Hair',
                'description': 'Top side hair reaches eyebrow or longer.',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/116_long.png',
            }
        },
        'Direction':{
            'description': 'Please annotate the Direction of top and front side hair. (Ignore hair on the side of the head for now)',
            'url':'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/120_direction.png',
            'option1': {
                'title': 'Straight Downward',
                'description': 'Bang straight downward.',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/121_down.jpg',
            },
            'option2': {
                'title': 'Decline Downward',
                'description': 'Top side hair falls to one side at around 45 degrees.',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/122_sideDown.jpg',
            },
            'option3': {
                'title': 'Incline Upward',
                'description': 'Top side hair sticks mostly upward at around 45 degrees.',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/123_sideUp.jpg',
            },
            'option4': {
                'title': 'Horizontal left or right',
                'description': 'Hair combed or brushed mostly sideways.',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/124_horizontal.jpg',
            },
            'option5': {
                'title': 'Central parting',
                'description': 'Hairstyle where the hair is separated at one side.',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/125_centralParting.jpg',
            },
            'option6':{
                'title':'Side parting',
                'description': 'Top side hair reaches eyebrow or longer',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/126_sideParting.jpg',
            },
            'option7':{
                'title':'Upward',
                'description': 'Hair standing upward or brushed so that it mostly sticks up',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/128_upward.jpg',
            },
            'option8':{
                'title':'Backward',
                'description': 'Hair pulled back, exposing forehead',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/127_backward.jpg',
            }
        },
        'Curl_Level':{
            'description':'Please annotate the Curl level of top and front side hair. (Ignore hair on the side of the head for now)',
            'url':'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/130_curlyLevel.jpg',
            'option1': {
                'title': 'Straight',
                'description': 'Naturally straight hair.',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/131_straight.jpg',
            },
            'option2': {
                'title': 'Wavie',
                'description': 'Not quite straight and not completely curly. Also includes someone who has messy hair, or wet hair.',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/132_wavie.jpg',
            },
            'option3': {
                'title': 'Curly',
                'description': 'Ranges from a light curl to tight, curly tendrils. Looks springy.',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/133_curly.jpg',
            },
            'option4': {
                'title': 'Coiled',
                'description': 'Fine and thin or wiry and coarse, with densely packed coils. ',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/134_Coiled.jpg',
            }
        }
    },
    'Side':{
        'description':'Please annotation hair on side of the head',
        'url':'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/200_side.jpg',
        'Length':{
            'description':'Please annotate the length on side of the head. Focus on the absolute hair length, regardless of gender. (Ignore hair on the top of the head for now)',
            'url':'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/210_length.png',
            'option1': {
                'title': 'Very Short',
                'description': 'Hair mostly shaved on the side. Bristly, like the surface of a brush. For example, undercut',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/211_veryShort.jpeg',
            },
            'option2': {
                'title': 'Short',
                'description': 'Natural wind can’t mess up this hair.',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/212_short.png',
            },
            'option3': {
                'title': 'Medium short hair',
                'description': 'Longer than short hair, but without covering the ear.',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/213_mediumShort.jpg',
            },
            'option4': {
                'title': 'Medium Long hair',
                'description': 'Length ranges from covering the ear to reaching the shoulder.',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/214_mediumLong.jpg',
            },
            'option5': {
                'title': 'Long hair',
                'description': 'Hair can stay on the shoulders and longer.',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/215_long.jpg',
            }
        },
        'Curl_Level':{
            'description':'Please annotate the Curl level of top and front side hair. (Ignore hair on the side of the head for now)',
            'url':'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/220_curlyLevel.jpg',
            'option1': {
                'title': 'Straight',
                'description': 'Naturally straight hair.',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/221_straight.jpg',
            },
            'option2': {
                'title': 'Wavie',
                'description': 'Not quite straight and not completely curly. Also includes someone who has messy hair, or wet hair.',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/222_wavie.jpg',
            },
            'option3': {
                'title': 'Curly',
                'description': 'Ranges from a light curl to tight, curly tendrils. Looks springy.',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/223_curly.jpg',
            },
            'option4': {
                'title': 'Coiled',
                'description': 'Fine and thin or wiry and coarse, with densely packed coils. ',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/224_Coiled.jpg',
            }
        },
    },
    'Braid':{
        'description':'Please annotation their briad, click no briad if they don’t have any',
        'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/300_braid.png',
        'Yes_No_Braid': {
            'description': 'The person used some threads, hair band to tie up his hair.',
            'url':'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/310_yesNo.png',
            
            'option1': {
                'title': 'No',
                'description': 'They are not wearing a braid.',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/311_no.jpg',
            },
            'option2': {
                'title': 'Yes',
                'description': 'They are wearing a braid.',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/311_yes.png',
            },
        },
        'Count':{
            'description': 'How many braids does the person have?',
            'url':'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/320_count.png',
            'option1': {
                'title': 'No braid',
                'description': 'They have No braid.',
                'url':''
            },
            'option2': {
                'title': 'Single',
                'description': 'There is only one braid. For example ponytail.',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/321_single.png',
            },
            'option3': {
                'title': 'Double',
                'description': 'There are two braids. For example double bun.',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/322_double.jpeg',
            },
            'option4': {
                'title': 'Multiple',
                'description': 'There are more than two braids. For example Dreadlock.',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/323_multiple.png',
            },
        },
        'Position':{
            'description': 'The braid position is high or low.',
            'url':'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/330_position.jpeg',
            'option1': {
                'title': 'No braid',
                'description': 'They have No braid.',
                'url':''
            },
            'option2': {
                'title': 'Low',
                'description': 'They have the briad at the lower side of his head.',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/331_low.jpeg',
            },
            'option3': {
                'title': 'High',
                'description': 'They have the briad at the upper side of his head.',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/332_high.png',
            }
        },
        'Braid_Style':{
            'description': 'What kind of braid is worn?',
            'url':'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/340_style.png',
            'option1': {
                'title': 'No braid',
                'description': 'They have No braid.',
                'url':''
            },
            'option2': {
                'title': 'Ponytail',
                'description': 'Hair tied at the back of the head, causing it to hang down like a tail of pony.',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/341_ponytail.png',
            },
            'option3': {
                'title': 'Plaited',
                'description': 'One or more braids, plaited or interlaced. ',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/342_plaited.png',
            },
            'option4': {
                'title': 'Deadlock',
                'description': 'A narrow ropelike strand of hair formed by matting, braiding, or twisting ',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/343_deadlock.png',
            },
            'option5': {
                'title': 'Bun',
                'description': 'Hair wrapped in a circular coil around itself. ',
                'url': 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/344_bun.png',
            }

        }
    }
}

# dump data_dict to json
with open('description.json', 'w') as f:
    json.dump(data_dict, f)

# import data_utils


# image_dir =  '/Users/minghaoliu/Desktop/HITL_navi/Turk/icon'
# image_paths = data_utils.make_im_set(image_dir)
# image_paths.sort()
# url_root = 'https://minghaouserstudy.s3.amazonaws.com/HITL_navi/icon/'

# for image_path in image_paths:
#     name = image_path.split('/')[-1]
#     url = url_root + name
#     print(url)
    

# data: {
#        'Top And Front': [
#                {name: 'length', check: false},
#                {name: 'category2', check: false},
#                {name: 'category3', check: false},
#            ],
#        'Side': [
#                {name: 'category4', check: false},
#                {name: 'category5', check: false},
#            ],
#        'Braid': [
#            {name: 'category6', check: false},
#            {name: 'category7', check: false},
#            {name: 'category8', check: false},
#            {name: 'category9', check: false},
#            {name: 'category10', check: false},
#        ],
#    }
