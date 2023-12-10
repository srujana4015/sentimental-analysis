from tkinter import *
import csv
from textblob import TextBlob


#Searching the product
with open('amazonreview44.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    product_set = set();
    for row in csv_reader:
        product_set.add(row[6])

    print("Product List: ")
    product_set.remove("name")
    for items in product_set:
        pass
        #print("\t", items)

OPTIONS = list(product_set)

top = Tk()
top.title("Customer Review Analysis")
top.geometry("1280x720")
top.config(background='black')
frame = Frame(top, bg='black')
frame.grid(row=0, column=0)

review_analysis_label = Label(frame, text="Review Analysis of Product", font="Times 40" , fg="blue", bg='black', width=45)
review_analysis_label.grid(row=0,column=0, columnspan=4)

select_product_label = Label(frame, text="Select the product: ", bg='black', fg='cyan')
select_product_label.grid(row=1, column=0, columnspan=4)

variable = StringVar(frame)
variable.set(OPTIONS[0]) # default value

w = OptionMenu(frame, variable, *OPTIONS)
w.grid(row=2, column=0, columnspan=4)
w.config(bg='black', fg='cyan', activebackground='black', activeforeground='cyan')
product_input = "null"






def ok():
    #print("value is:" + variable.get())
    #product_input = variable.get()
    product_input = variable.get()


    # Start of the review Analysis code

    sent_code = 0.0
    with open('amazonreview44.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # product_input = input("\n\tEnter the name of the product you want to search: ")
        searched_pid = "null"
        for row in csv_reader:
            if product_input in row[6]:
                print("\nProduct found:\t {}".format(row[6]))
                searched_pid = row[0]
                break

        if searched_pid == "null":
            print("Item Not Found! Please Enter the correct Keyword! \n\n")
            exit()

    max_pos_rev = "null"
    min_pos_rev = "null"

    max_pos_rev_num = -1
    min_pos_rev_num = 1

    top_pos_username = "null"
    top_neg_username = "null"

    overall_rating = 0

    with open('amazonreview44.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue
            else:
                if (row[0] == searched_pid):
                    # lst.append(row[2])

                    # Get the article
                    article = row[3]

                    # Create a text blob object
                    obj = TextBlob(article)
                    overall_rating += int(row[2])
                    sentiment = obj.sentiment.polarity

                    if sentiment > max_pos_rev_num:
                        max_pos_rev_num = sentiment
                        max_pos_rev = row[3]
                        top_pos_username = row[5]
                    if sentiment < min_pos_rev_num:
                        min_pos_rev_num = sentiment
                        min_pos_rev = row[3]
                        top_neg_username = row[5]

                    sent_code += sentiment
                    line_count += 1

    # print(max_pos_rev_num)
    # print(min_pos_rev_num)
    print("\n\nTop Positive review with a sentiment of: {:.2f} \n\t{} \t by {}".format(max_pos_rev_num, max_pos_rev,
                                                                                       top_pos_username))
    print("\n\nTop Negative review with a sentiment of: {:.2f} \n\t{} \t by {}".format(min_pos_rev_num, min_pos_rev,
                                                                                       top_neg_username))

    print(f'\n\nTotal Number of reviews analysed:  {line_count} ')
    overall_analysis = sent_code / line_count
    print("\n\nFinal Sentiment: (Scale: -1 means worst and 1 means best): \t{:.2f}\n\n".format(overall_analysis))

    if overall_analysis > 0.4:
        final_verdict = "The product is excellent and don't hazitate to buy the product!"
    elif overall_analysis > 0.35:
        final_verdict = "The product is better and it is highly recommended to buy!"
    elif overall_analysis > 0.3:
        final_verdict = "The product is good and you have made a correct choice!"
    elif overall_analysis > 0.25:
        final_verdict = "The product is Okey and you are not going to regret."
    elif overall_analysis > 0.2:
        final_verdict = "The product is quiet good and you can buy it!"
    elif overall_analysis > 0.15:
        final_verdict = "The product is usable but think twice before buying it."
    elif overall_analysis > 0.1:
        final_verdict = "The product is somehow manageable but you can look around for other similar products"
    elif overall_analysis > 0.0:
        final_verdict = "The product is neutral and it can be good or bad piece depending on your luck!"
    elif overall_analysis > 0.5:
        final_verdict = "The product is not recomended at all!"
    else:
        final_verdict = "The product is worse, Don't buy it ever!"

    print("Overall Rating of the product is {:.2f} out of 5".format(overall_rating / line_count))



    ###########################################################
    pos_frame = Frame(frame, highlightbackground="green", highlightcolor="green", highlightthickness=2)
    pos_frame.grid(row=5, column=0, columnspan=2)

    top_pos_rev_label = Label(pos_frame, text="", font="Times 12", fg="green", bg='black', wraplengt=400, height=17,
                              width=50)
    top_pos_rev_label.grid(row=5, column=0, columnspan=4)

    neg_frame = Frame(frame, highlightbackground="red", highlightcolor="red", highlightthickness=2)
    neg_frame.grid(row=5, column=2, columnspan=2)
    # pos_frame.config(bg="pink")
    top_neg_rev_label = Label(neg_frame, text="", font="Times 12", fg="red", bg='black', wraplengt=400, height=17,width=50)
    top_neg_rev_label.grid(row=6, column=0, columnspan=4)

    empty_frame = Frame(frame)
    empty_frame.grid(row=6)
    empty_label = Label(empty_frame, text="", bg='black')
    empty_label.grid(row=6)

    result_frame = Frame(frame,bg='black', highlightbackground="cyan", highlightcolor="cyan", highlightthickness=2, pady=5)
    result_frame.grid(row=7, column=0, columnspan=4)
    total_review_analyzed_label = Label(result_frame, text="", font="Times 12", fg="cyan", bg='black')
    total_review_analyzed_label.grid(row=7, column=0, columnspan=4)

    final_sentiment_label = Label(result_frame, text="", font="Times 12", fg="cyan", bg='black')
    final_sentiment_label.grid(row=8, column=0, columnspan=4)

    final_rating_label = Label(result_frame, text="", font="Times 12", fg="cyan", bg='black')
    final_rating_label.grid(row=9, column=0, columnspan=4)

    final_verdict_label = Label(result_frame, text="", font="Times 20", fg="magenta", bg='black', width=75)
    final_verdict_label.grid(row=10, column=0, columnspan=4)
    #######################################################



    product_found_label['text'] = "\nAnalyzing product... {}".format(product_input)
    top_pos_rev_label['text'] = "\n\nTop positive review with a sentiment of: {:.2f}\n\n\t{}\n by...  {}".format(max_pos_rev_num, max_pos_rev, top_pos_username)
    top_neg_rev_label['text'] = "\n\nTop negative review with a sentiment of: {:.2f}\n\n\t{}\n by...  {}".format(min_pos_rev_num, min_pos_rev, top_neg_username)
    total_review_analyzed_label['text'] = "\nTotal number of reviews analyzed:   {}".format(line_count)
    final_sentiment_label['text'] = "\nFinal Sentiment: (Scale: -1 means worst and 1 means best):  {:.2f}".format(overall_analysis)
    final_rating_label['text'] = "\nOverall Rating of the product is {:.2f} out of 5".format(overall_rating / line_count)
    final_verdict_label['text'] = "Final Verdict:  {}".format(final_verdict)
    # End of ra code

    #overall_analysis_label = Label(frame,"\n\nFinal Sentiment: (Scale: -1 means worst and 1 means best): \t{:.2f}".format(overall_analysis), font="Times 12", fg="blue")
    #overall_analysis_label.grid(row=7, column=0)

button = Button(frame, text="Analyze...",command=ok, bg="green", fg="white", activebackground='green', activeforeground='black')
button.grid(row=3, column=0, columnspan=4)

#product_image_label = Label(frame, text="Arbind Kumar")
#product_image_label.grid(row=4, column=3, rowspan=4)


# Output on the gui
product_found_label = Label(frame, text="", font="Times 10", fg="cyan", bg='black')
product_found_label.grid(row=4, column=0, columnspan=4)




print(product_input)
top.mainloop()











    #print("\n\n\nEnter the name of the product or a unique keyword for the name\n\t For example type   \"Echo Plus\" for \"Amazon - Echo Plus w/ Built-In Hub - Silver\"")











