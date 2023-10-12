from context import prosomoiahelper

texts = []

texts.append("""Patriarch Germanos the New assembled * the accounts of all of the Seven Councils * convened by
the Fathers at diverse times and compiled them * into a single rule and canon, setting them all in
order. * He thus confirmed their doctrines, gath’ring them in one written record. * He established them as fellow shepherds * o’er us the flock and as most vigilant suppliants * before the Lord, that
we may be saved.""")

texts.append("""The Law’s letter bound the sons of the Hebrews * to observe the seventh day with due
rev’rence, * and keeping that worship, they persisted in the shadow. * And when ye gathered in
the Seven Councils, O sacred Fathers, * bade thus by God, Who finished all His works in a span
of six days * and thereafter also blessed the seventh, * ye made the seventh yet more hallowed and
ven’rable * when ye decreed the bounds of the Faith.
""")

texts.append("""To all men ye clearly bequeathed the teaching * that the Holy Trinity is the Cause of * the world’s
generation, as His works plainly declare Him; * for, being mysticly inspired, ye called three and
four great Councils, * proving the champions of Orthodoxy, O thrice-blessed Fathers, * and ye
showed that the God of Three Persons * is our Creator Who hath made the four elements * and
fashioned all of the universe.""")

texts.append("""It would have sufficed Prophet Elisseus * to bend down but once that he thus might quicken * and
breathe life again in the dead son of her that served him; * rather, he knelt down seven times, and
seven times bowed upon him. * Thus, in his forevision, he prophesied of your seven
gath’rings, * in the which ye breathed your quick’ning word on * the death of God the Word, and
put to death Arius * and his profane fellow-laborers.
""")

texts.append("""Christ the Savior’s garment, which had been sundered, * rent apart by dogs shameless in their
barking, * ye wisely have mended, O ye venerable Fathers, * in no wise bearing to behold the
nakedness of your Master, * as Shem and Japheth hid their father’s nakedness once
aforetime. * Thus ye shamed that slayer of his father, * the wretched Arius, the namesake of
frenziedness, * and those of like mind and thought with him.""")

texts.append("""Each and every Eutyches and Sabellius, * and Apollinarius and Nestorius, * Dioscorus, lawless
Macedonius, and Sev’rus, * all who were shown forth to be grievous wolves in sheep’s clothing
hidden, * ye as true shepherds drove far off from the flock of Christ the Savior, * when ye stripped
them naked of their sheepskins * and nobly overcame those thrice-wretched heretics; * wherefore
we rightfully call you blest.""")

added_melismas = [116]
ignored_melismas = list()
word_overrides_by_index = dict()

for i, text in enumerate(texts):
    if i == 1:
        word_overrides_by_index[65] = ['blessed']
    elif i == 2:
        ignored_melismas = [77]        
    elif i == 5:
        ignored_melismas = [14, 27]


    prosomoiahelper.generate_prosomoia(
        text, 
        'example_2__input.byzx', 
        f'example_2__output_{i+1}.byzx', 
        ignored_melismas=ignored_melismas, 
        added_melismas=added_melismas, 
        word_overrides_by_index=word_overrides_by_index,
        print_syllable_index=True,
        print_word_index=False)