from django.http import HttpResponseRedirect
from django.shortcuts import render
from dbserver.models import AST


# Create your views here.


def all_control_works(request):
    if request.user.is_authenticated:
        all_user_schemas = request.user.data_schemas.split()
        all_ast_queries = AST.objects.all()
        all_ast_sec_queries = all_ast_queries.values('db_index', 'db_request')
        # for ast_query in all_ast_queries:
        #     print("{} {} {}".format(ast_query.db_index, ast_query.db_request, ast_query.db_answer))
        print(all_ast_sec_queries)
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
        print(schema)
    else:
        return HttpResponseRedirect('/account/login/')