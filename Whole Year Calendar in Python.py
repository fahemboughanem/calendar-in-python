{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ca8d3038",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter year:2023\n",
      "                                                  2023\n",
      "\n",
      "      January                     February                     March                       April\n",
      "Mo Tu We Th Fr Sa Su        Mo Tu We Th Fr Sa Su        Mo Tu We Th Fr Sa Su        Mo Tu We Th Fr Sa Su\n",
      "                   1               1  2  3  4  5               1  2  3  4  5                        1  2\n",
      " 2  3  4  5  6  7  8         6  7  8  9 10 11 12         6  7  8  9 10 11 12         3  4  5  6  7  8  9\n",
      " 9 10 11 12 13 14 15        13 14 15 16 17 18 19        13 14 15 16 17 18 19        10 11 12 13 14 15 16\n",
      "16 17 18 19 20 21 22        20 21 22 23 24 25 26        20 21 22 23 24 25 26        17 18 19 20 21 22 23\n",
      "23 24 25 26 27 28 29        27 28                       27 28 29 30 31              24 25 26 27 28 29 30\n",
      "30 31\n",
      "\n",
      "        May                         June                        July                       August\n",
      "Mo Tu We Th Fr Sa Su        Mo Tu We Th Fr Sa Su        Mo Tu We Th Fr Sa Su        Mo Tu We Th Fr Sa Su\n",
      " 1  2  3  4  5  6  7                  1  2  3  4                        1  2            1  2  3  4  5  6\n",
      " 8  9 10 11 12 13 14         5  6  7  8  9 10 11         3  4  5  6  7  8  9         7  8  9 10 11 12 13\n",
      "15 16 17 18 19 20 21        12 13 14 15 16 17 18        10 11 12 13 14 15 16        14 15 16 17 18 19 20\n",
      "22 23 24 25 26 27 28        19 20 21 22 23 24 25        17 18 19 20 21 22 23        21 22 23 24 25 26 27\n",
      "29 30 31                    26 27 28 29 30              24 25 26 27 28 29 30        28 29 30 31\n",
      "                                                        31\n",
      "\n",
      "     September                    October                     November                    December\n",
      "Mo Tu We Th Fr Sa Su        Mo Tu We Th Fr Sa Su        Mo Tu We Th Fr Sa Su        Mo Tu We Th Fr Sa Su\n",
      "             1  2  3                           1               1  2  3  4  5                     1  2  3\n",
      " 4  5  6  7  8  9 10         2  3  4  5  6  7  8         6  7  8  9 10 11 12         4  5  6  7  8  9 10\n",
      "11 12 13 14 15 16 17         9 10 11 12 13 14 15        13 14 15 16 17 18 19        11 12 13 14 15 16 17\n",
      "18 19 20 21 22 23 24        16 17 18 19 20 21 22        20 21 22 23 24 25 26        18 19 20 21 22 23 24\n",
      "25 26 27 28 29 30           23 24 25 26 27 28 29        27 28 29 30                 25 26 27 28 29 30 31\n",
      "                            30 31\n",
      "\n"
     ]
    },
    {
     "ename": "AttributeError",
     "evalue": "'function' object has no attribute 'png'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "Cell \u001b[0;32mIn [2], line 4\u001b[0m\n\u001b[1;32m      2\u001b[0m year\u001b[38;5;241m=\u001b[39m \u001b[38;5;28mint\u001b[39m(\u001b[38;5;28minput\u001b[39m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mEnter year:\u001b[39m\u001b[38;5;124m'\u001b[39m))\n\u001b[1;32m      3\u001b[0m \u001b[38;5;28mprint\u001b[39m(calendar(year, \u001b[38;5;241m2\u001b[39m, \u001b[38;5;241m1\u001b[39m, \u001b[38;5;241m8\u001b[39m, \u001b[38;5;241m4\u001b[39m))\n\u001b[0;32m----> 4\u001b[0m \u001b[43mcalendar\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mpng\u001b[49m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcalendar\u001b[39m\u001b[38;5;124m\"\u001b[39m, scale\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m5\u001b[39m)\n",
      "\u001b[0;31mAttributeError\u001b[0m: 'function' object has no attribute 'png'"
     ]
    }
   ],
   "source": [
    "from calendar import*\n",
    "year= int(input('Enter year:'))\n",
    "print(calendar(year, 2, 1, 8, 4))\n",
    "calendar.png(\"calendar\", scale=5)\n",
    "#2=2 characters for days (Mu,Tu,etc)\n",
    "#1 = 1 line (row) for each week\n",
    "#8 = 8 rows for each month\n",
    "#4 = 4 columns for all months of the year.\n",
    "\n",
    "#Fahimo.com\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9b4a26c0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
