def get_valid_data(model_data_object, model_class):
    data_dict = {}
    for column in model_class._meta.fields:
        data_dict[column] = getattr(model_data_object, column)
    return data_dict
