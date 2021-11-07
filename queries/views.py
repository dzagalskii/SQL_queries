from django.http import HttpResponseRedirect
from django.shortcuts import render
from dbserver.models import AST


# Create your views here.


def all_queries(request):
    if request.user.is_authenticated:
        all_user_schemas = request.user.data_schemas.split()
        all_ast_queries = AST.objects.all()
        all_ast_sec_queries = all_ast_queries.values('db_index', 'db_request')
        # for ast_query in all_ast_queries:
        #     print("{} {} {}".format(ast_query.db_index, ast_query.db_request, ast_query.db_answer))
        print(all_ast_sec_queries)
        return render(request, 'all_queries.html',
                      {'img_1': 'img/' + all_user_schemas[0] + '.jpg',
                       'img_2': 'img/' + all_user_schemas[1] + '.jpg',
                       'img_3': 'img/' + all_user_schemas[2] + '.jpg'})
    else:
        return HttpResponseRedirect('/account/login/')
