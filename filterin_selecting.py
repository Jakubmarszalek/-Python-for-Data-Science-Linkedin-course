import numpy as np
import pandas as pd
from pandas import Series, DataFrame


def lesson_2_1():
    series_obj = Series(np.arange(8), index=["row 1", "row 2", "row 3", "row 4", "row 5", "row 6", "row 7", "row 8"])
    print(series_obj)
    print(series_obj["row 7"])
    print(series_obj[[0,7]])
    np.random.seed(25)
    DF_obj = DataFrame(np.random.rand(36).reshape((6, 6)),
                   index=["row1", "row2", "row3", "row4", "row5", "row6"],
                   columns=["column1", "column2", "column3", "column4", "column5", "column6"])
    print(DF_obj)
    print(DF_obj.loc[["row2", "row5"], ["column1", "column2"]])
    print(series_obj["row 3":"row 7"])
    print(DF_obj < .2)
    print(series_obj[series_obj > 6])
    series_obj["row 1", "row 5", "row 8"] = 8
    print(series_obj)


def lesson_2_2():
    missing = np.nan
    series_obj = Series(["row 1", "row 2", missing, "row 4", "row 5", "row 6", missing, "row 8"])

    DF_obj =DataFrame(np.random.rand(36).reshape(6,6))
    DF_obj.loc[3:5, 0] = missing
    DF_obj.loc[1:4, 5] = missing
    filled_DF = DF_obj.fillna(0)
    filled_DF = DF_obj.fillna({0: 0.1, 5: 1.25})
    filled_DF = DF_obj.fillna(method="ffill")
    print(DF_obj)
    DF_obj = DF_obj.isnull().sum()
    print(DF_obj)


def lesson_2_3():
    DF_obj = DataFrame({"column1": [1, 1, 2, 2, 3, 3, 3],
                        "column2": ["a", "a", "b", "b", "c", "c", "c"],
                        "column3": ["A", "A", "B", "B", "C", "C", "C"]})
    print(DF_obj.duplicated())
    print(DF_obj)
    print(DF_obj.drop_duplicates())
    print(DF_obj.drop_duplicates(["column3"]))


def lesson_2_4():
    DF_obj = pd.DataFrame(np.arange(36).reshape(6, 6))
    DF_obj_2 = pd.DataFrame(np.arange(15).reshape(5, 3))
    print(DF_obj)
    print(DF_obj_2)
    object = pd.concat([DF_obj, DF_obj_2])
    object = DF_obj.drop([0, 2], axis=1) #axis =1 cut column not row
    object = Series(np.arange(6))
    object.name = "added"
    object2 = object.append(object, ignore_index=False)
    print(DF_obj)
    object = DF_obj.sort_values(by=(5), ascending=[False])
    print(object)


def lesson_2_5():
    adderss = "C:/Users/krajmr/desktop/Exercises/Data/mtcars.csv"

    cars = pd.read_csv(adderss)

    cars.columns = ["car_names", "mpg", "cy1", "disp", "hp", "drat", "wt", "qsec"]
    cars.head()
