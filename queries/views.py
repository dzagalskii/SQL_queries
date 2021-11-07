from random import randint

from django.http import HttpResponseRedirect
from django.shortcuts import render
from dbserver.models import AST


# Create your views here.


def all_control_works(request):
    if request.user.is_authenticated:
        all_user_schemas = request.user.data_schemas.split()
        return render(request, 'all_control_works.html',
                      {'img_1': 'img/' + all_user_schemas[0] + '.jpg',
                       'img_2': 'img/' + all_user_schemas[1] + '.jpg',
                       'img_3': 'img/' + all_user_schemas[2] + '.jpg'})
    else:
        return HttpResponseRedirect('/account/login/')


def control_work(request, control_work_id):
    control_work_id = int(control_work_id)
    if request.user.is_authenticated:
        if control_work_id != 1 and control_work_id != 2 and control_work_id != 3:
            return HttpResponseRedirect('/queries')
        all_user_schemas = request.user.data_schemas.split()
        schema = all_user_schemas[control_work_id - 1]

        # if schema == 'AST':
        #     all_queries = AST.objects.all()
        # elif schema == 'SPJ':
        #     all_queries = SPJ.objects.all()
        # elif schema == 'WF':
        #     all_queries = WF.objects.all()

        all_queries = AST.objects.all()
        all_sec_queries = all_queries.values('db_index', 'db_request')

        random_three_queries = []
        for i in range(3):
            random_three_queries.append(all_sec_queries[randint(0, len(all_sec_queries) - 1)])
        print(random_three_queries)

        return render(request, 'control_work.html',
                      {'control_work_id': control_work_id,
                       'img': 'img/' + all_user_schemas[control_work_id - 1] + '.jpg',
                       'random_three_queries': random_three_queries})

        # all_ast_sec_queries = all_queries.values('db_index', 'db_request')
        # for ast_query in all_ast_queries:
        #     print("{} {} {}".format(ast_query.db_index, ast_query.db_request, ast_query.db_answer))
        # print(all_ast_sec_queries)
    else:
        return HttpResponseRedirect('/account/login/')
