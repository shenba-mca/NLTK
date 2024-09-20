import csv
fields=["Quotes","Author"]
rows=[
    ["There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.","Albert Einstein"],
    ["Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.","Marilyn Monroe"],
    ["I have not failed. I've just found 10,000 ways that won't work.","Thomas A. Edison"],
    ["The opposite of love is not hate, it's indifference. The opposite of art is not ugliness, it's indifference. The opposite of faith is not heresy, it's indifference. And the opposite of life is not death, it's indifference.","Elie Wiesel"],
    ["To the well-organized mind, death is but the next great adventure.","J.K. Rowling"],
    ["It is never too late to be what you might have been.","George Eliot"],
    ["You can never get a cup of tea large enough or a book long enough to suit me.","C.S. Lewis"],
    ["Only in the darkness can you see the stars.","Martin Luther King Jr."],
    ["When one door of happiness closes, another opens; but often we look so long at the closed door that we do not see the one which has been opened for us.","Martin Luther King Jr."],
    ["When one door of happiness closes, another opens; but often we look so long at the closed door that we do not see the one which has been opened for us.","Helen Keller"]
    ]
with open("file.csv",'w') as csv_file:
    writer = csv.writer(csv_file)
    # Write the header
    writer.writerow(fields)
    writer.writerows(rows)