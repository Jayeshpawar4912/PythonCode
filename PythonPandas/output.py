Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\JAYESH PAWAR\OneDrive\Desktop\python\PythonPandas\Pandas.py
..........Python Pandas...............
Series
0    p
1    a
2    n
3    d
4    a
5    s
dtype: object


Retrieving Dimension,Size,and number of Bytes
1 1
4 6
32 48


....DataFrames...
Empty DataFrame
Columns: []
Index: []

        0
0  Pandas
1  Python

    ID Department
0  101       B.sc
1  102     B.tech
2  103     M.Tech

   One  two
a    1  1.0
b    2  2.0
c    3  3.0
d    4  4.0
e    5  NaN
f    6  NaN


Column Selction
a    1
b    2
c    3
d    4
e    5
f    6
Name: One, dtype: int64


Column Addition
Add new Column
   One  two  Three  four
a    1  1.0   20.0  21.0
b    2  2.0   30.0  32.0
c    3  3.0   40.0  43.0
d    4  4.0   50.0  54.0
e    5  NaN   60.0  65.0
f    6  NaN    NaN   NaN


Column Deletion
Delete the One column:
   two  Three  four
a  1.0   20.0  21.0
b  2.0   30.0  32.0
c  3.0   40.0  43.0
d  4.0   50.0  54.0
e  NaN   60.0  65.0
f  NaN    NaN   NaN
Delete the another column
   two  four
a  1.0  21.0
b  2.0  32.0
c  3.0  43.0
d  4.0  54.0
e  NaN  65.0
f  NaN   NaN


Appends Function
    x   y     z
0  25  47   NaN
1  15  24   NaN
2  12  17   NaN
3  19  29   NaN
0  25  47  38.0
1  15  24  12.0
2  12  17  45.0


Apply Function
          p         q
0  1.414214  2.645751
1  1.414214  2.645751
2  1.414214  2.645751
3  1.414214  2.645751


....Aggregate Function......
        x     y     z
sum  29.0  38.0  46.0
min   1.0   5.0   7.0
max  18.0  21.0  24.0


....Sort Function......
  col4 col3
1  NaN  NaN
2  NaN  NaN
5  NaN  NaN
4  NaN  NaN
7  NaN  NaN
9  NaN  NaN
3  NaN  NaN
0  NaN  NaN
6  NaN  NaN
8  NaN  NaN
   col4  col3
0    30   300
1    10   100
2    20   200
3    90   900
4    40   400
5    50   500
6     0     0
7    80   800
8    60   600
9    70   700


....Sum Function for DataFrame......
Original DataFrames:
     A    B     C
0  1.0  4.0  None
1  2.0  NaN  None
2  3.0  6.0  None
3  NaN  7.0  None

 Column_wise sum(min.count=0):
A     6.0
B    17.0
C       0
dtype: object
     A    B     C
0  1.0  4.0  None
1  2.0  NaN  None


....Join Function......
  key_caller   A keyx    B
0         k0  A0   k0   B0
1         k1  A1   k1   B1
2         k2  A2   k2   B2
3         k3  A3  NaN  NaN
4         k4  A4  NaN  NaN
5         k5  A5  NaN  NaN


....Rename Function......
  Key   A
0  k0  A0
1  k1  A1
2  k2  A2
3  k3  A3
4  k4  A4
5  k5  A5


....Pivot_table Function......
Empty DataFrame
Columns: []
Index: [(k0, A0), (k1, A1), (k2, A2), (k3, A3), (k4, A4), (k5, A5)]
