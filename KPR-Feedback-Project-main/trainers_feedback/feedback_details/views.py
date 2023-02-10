from django.shortcuts import render
from django.http import HttpResponse
from feedback_details.models import trainer_data, trainer_feedback
import json
# Create your views here.


def index(request):
    # Trainer data set
    trainer_list = trainer_data.objects.all()
    trainer_list_json = json.dumps(list(trainer_list.values()))

    # List to score the variables

    average_score = []
    name_list = []
    communication = []
    content = []
    doubt = []
    technical = []

    # checking the database

    temp = trainer_data.objects.get(id="EM0005")
    print(temp.name)

    # Caculating the average score

    for trainer in trainer_list:
        feed_details = trainer_feedback.objects.filter(train_id=trainer.id)
        name_list.append(trainer.name)
        average = 0
        # print("Name :", trainer.name)
        count = 0
        com_average = 0
        content_average = 0
        doubt_average = 0
        tech_average = 0

        # Iterating through all the train_id
        for feed in feed_details:
            # print("feed :", feed.train_id)
            average += feed.communicatin_skill + feed.content_delivered + \
                feed.doubt_clarification + feed.technical_skill
            count += 1
            com_average += feed.communicatin_skill
            content_average += feed.content_delivered
            doubt_average += feed.doubt_clarification
            tech_average += feed.technical_skill
        try:
            average_score.append(int(average/count))
            communication.append(com_average/count)
            content.append(content_average/count)
            doubt.append(doubt_average/count)
            technical.append(tech_average/count)
        except:
            average_score.append(0)
            communication.append(0)
            content.append(0)
            doubt.append(0)
            technical.append(0)

    # Conveerting list to JSON

    name_list_json = json.dumps(name_list)
    average_score_json = json.dumps(average_score)
    communication_json = json.dumps(communication)
    content_json = json.dumps(content)
    doubt_json = json.dumps(doubt)
    technical_json = json.dumps(technical)

    # Zipping the average score and name of the trainer
    table_zip = zip(average_score, trainer_list)

    dic = {
        'table_zip': table_zip, 'scores': average_score, 'trainer_data': trainer_list,
        "trainer_list_json": trainer_list_json, "average_score_json": average_score_json,
        "communication_json": json.dumps(communication), "content_json": json.dumps(content),
        "doubt_json": json.dumps(doubt), "technical_json": json.dumps(technical)}

    return render(request, 'index.html', dic)

def feedback(request):
    return render(request, 'feedback.html')