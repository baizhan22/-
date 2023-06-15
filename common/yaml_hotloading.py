import json
import jsonpath
from common.public_util import Public


class Hot_Loading:

    def loading_ccnfig(self,**kwargs):
        data_type=type(kwargs)
        if isinstance(kwargs,dict) or isinstance(kwargs,list):
            str_data=json.dumps(kwargs)
        else:
            str_data=str(kwargs)
        for i in range(1,str_data.count('${')+1):
            if "${" in str_data and "}" in str_data:
                index=str_data.index("${")
                end=str_data.index('}',index)
                v=str_data[index:end+1]
                name=v[2:v.index('(')]
                values=v[v.index('(')+1:v.index(')')]
                values_new = values.split(",")
                if values_new[0] !='':
                    new_value=getattr(Public(),name)(*values_new)
                    if type(new_value) == list:
                        str_data = str_data.replace(v, str(new_value[0]))
                    else:
                        str_data = str_data.replace(v, str(new_value))
                else:
                    new_value = getattr(Public(), name)()
                    if type(new_value)==list:
                        str_data = str_data.replace(v, str(new_value[0]))
                    else:
                        str_data = str_data.replace(v, str(new_value))
        if isinstance(kwargs, dict) or isinstance(kwargs, list):
            kwargs= json.loads(str_data)
        else:
            kwargs=str_data
        return kwargs

    def jsonpth_config(self,respons,**kwargs):
        if kwargs.get('extract') !=None:
            for i in kwargs.get('extract'):
                for key,value in i.items():
                    if '$.' in value:
                        w=jsonpath.jsonpath(respons.json(),value)
                        Public().write_extract_yaml({key:w[0]})
            return 1
        else:
            return None