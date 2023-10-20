import json
import pyphen
import zipfile

default_overrides__en_US = {

# Names
"apollinarius": "a-pol-lin-ar-i-us",
"arius": "ar-i-us",
"averkios": "a-ver-ki-os",
"cleopas": "cle-o-pas",
"dioscorus": "di-o-scor-us",
"elisseus": "el-is-se-us",
"emmaus": "em-ma-us",
"germanos": "ger-man-os",
"japheth": "japh-eth",
"macedonius": "mac-e-don-i-us",
"nestorius": "nes-tor-i-us",
"pelagia": "pel-a-gi-a",
"sabellius": "sab-el-li-us",
"sev'rus": "sev'-rus",
"sion": "si-on",

"abode": "a-bode",
"added": "add-ed",
"aforetime": "a-fore-time",
"alabaster": "al-a-bas-ter",
"again": "a-gain",
"alone": "a-lone",
"anew": "a-new",
"apart": "a-part",
"apostle": "a-pos-tle",
"apostles": "a-pos-tles",
"arising": "a-ris-ing",
"asleep": "a-sleep",
"beheldest": "be-held-est",
"blessed": "bless-ed",
"body": "bod-y",
"canon": "can-on",
"comforter": "com-fort-er",
"covenant": "cov-en-ant",
"creator": "cre-a-tor",
"demons": "de-mons",
"deeply": "deep-ly",
"diseases": "dis-eas-es",
"earnestly": "earn-est-ly",
"entreaties": "en-treat-ies",
"equal": "e-qual",
"even": "ev-en",
"fashioner": "fash-ion-er",
"fiery": "fier-y",
"fragrancy": "fra-gran-cy",
"fulfiller": "ful-fill-er",
"heldest": "held-est",
"heretics": "her-i-tics",
"giveth": "giv-eth",
"gospel": "gos-pel",
"guardeth": "guard-eth",
"greater": "great-er",
"healest": "heal-est",
"holy": "ho-ly",
"hon'rable": "hon'-ra-ble",
"illumineth": "il-lum-in-eth",
"inscriber": "in-scrib-er",
"knoweth": "know-eth",
"luminary": "lum-in-ar-y",
"madest": "ma-dest",
"maladies": "mal-a-dies",
"many": "man-y",
"marvelous": "mar-vel-ous",
"mysticly": "mys-tic-ly",
"mystery": "mys-ter-y",
"naked": "na-ked",
"nakedness": "na-ked-ness",
"noetic": "no-et-ic",
"nobly": "nob-ly",
"obedience": "o-be-di-ence",
"odor": "od-or",
"orthodoxy": "or-tho-dox-y",
"overcame": "o-ver-came",
"paradise": "par-a-dise",
"physician": "phys-i-cian",
"piety": "pi-e-ty",
"prophet": "proph-et",
"putting": "put-ting",
"quick'ning": "quick'-ning",
"raineth": "rain-eth",
"rather": "rath-er",
"record": "rec-ord",
"recorded": "re-cord-ed",
"recorder": "re-cord-er",
"revered": "rev-ered",
"rev'rence": "rev'-rence",
"sep'rately": "sep'-rate-ly",
"sov'reign": "sov'-reign",
"sundry": "sun-dry",
"tabernacle": "tab-er-na-cle",
"tablets": "tab-lets",
"taughtest": "taught-est",
"temp'rance": "temp'-rance",
"temp'rance": "temp'-rance",
"thereafter": "there-af-ter",
"treasury": "trea-sur-y",
"tyrant": "ty-rant",
"unaware": "un-a-ware",
"unerring": "un-err-ing",
"universe": "u-ni-verse",
"ven'rable": "ven'-ra-ble",
"virtue": "vir-tue",
}

default_overrides = dict()
default_overrides['en_US'] = default_overrides__en_US

def generate_prosomoia(text: str, input_path: str, output_path: str, overrides=dict(), word_overrides_by_index=dict(), ignored_melismas=list(), added_melismas=list(), print_syllable_index = False, print_word_index = False, lang = "en_US"):
    """
    Generates a prosomoia for a given text based on a given model melody in byzx format

    :param str text: The text of the prosomoia
    :param input_path str: The path to the file that contains the model melody
    :param output_path str: The path where the new file will be saved
    :param overrides dict: Overrides for the hyphenation. The key is the unhyphenated word and the value is hyphenated word (e.g. spir-it)
    :param ignored_melismas list: Indices of score elements that should not be treated as melismas, even though they are melismas in the input file
    :param added_melismas list: Indices of score elements that should be treated as melismas, even though they are not melismas in the input file
    :param print_syllable_index bool: If true, a list of syllables and their corresponding element indices will be printed
    :param lang str: The language to use for the hyphenation dictionary
    """
    words = __preprocess_text(text, overrides, word_overrides_by_index, print_word_index, lang)

    #read the file
    score = None

    if input_path.endswith('byz'):
        with zipfile.ZipFile(input_path) as z:
            with z.open(z.namelist()[0]) as f:
                score = json.load(f)
    elif input_path.endswith('byzx'):
        with open(input_path, 'r', encoding="utf-8") as f:
            score = json.load(f)
    else:
        raise Exception('Unrecognized file extension for input_path. Expected .byz or .byzx')

    print(f'Loaded {input_path}')

    word_index = 0
    syllable_index = 0
    fix_drop_cap = False

    # handle added melismas by clearing lyrics and setting isMelisma=True on the score element
    for i in added_melismas:
        e = score['staff']['elements'][i]
        if e['elementType'] == 'Note':
                e.pop('lyrics', None)
                e['isMelisma'] = True

    # loop through the score elements and assign lyrics
    for i, e in enumerate(score['staff']['elements']):
        # if we've run out of words, stop looping
        if word_index > len(words) - 1:
            break

        # handle drop caps:
        # if we found a drop cap at the beginning, then set
        # the drop cap value and set the fix_drop_cap flag 
        # so that we remember to fix the note lyrics later
        if word_index == 0 and e['elementType'] == 'DropCap':
            e['content'] = words[word_index][0][0]
            fix_drop_cap = True

        # if we found a note, assign lyrics to it
        # we only assign lyrics to notes that already have lyrics
        # or that are in our list of ignored melismas
        if e['elementType'] == 'Note' and ('lyrics' in e or i in ignored_melismas):
            took_syllable = False

            if __is_melisma(e):
                e['lyrics'] = words[word_index][syllable_index]
                took_syllable = True
            else:  
                e['lyrics'] = words[word_index][syllable_index]
                took_syllable = True

            if took_syllable:
                # if a drop cap stole our first letter, then we
                # remove the first letter from the lyrics to avoid
                # duplicate first letters
                if fix_drop_cap:
                    e['lyrics'] = e['lyrics'][1:]
                    fix_drop_cap = False

                if syllable_index == 0 and len(words[word_index]) > 1:
                    # if first of several syllables, then this is a hyphen melisma
                    e['isMelisma'] = True
                    e['isMelismaStart'] = True
                    e['isHyphen'] = True
                elif syllable_index == len(words[word_index]) - 1:
                    # if this is the last syllable, then
                    if i + 1 < len(score['staff']['elements']) - 1 and score['staff']['elements'][i+1]["elementType"] == "Note":
                        # if the next element is a melisma note, then this note is a melisma.
                        # this note is also a melisma if the next note is a running elaphron
                        is_melisma = not 'lyrics' in score['staff']['elements'][i+1] or score['staff']['elements'][i+1]["quantitativeNeume"] == "RunningElaphron" 
                        e['isMelisma'] = is_melisma
                        e['isMelismaStart'] =  is_melisma
                    else:
                        e['isMelisma'] = False
                        e['isMelismaStart'] = False
                    e['isHyphen'] = False
                else:
                    # if we are in the middle of a word, then we are a hyphen melisma
                    e['isMelisma'] = True
                    e['isMelismaStart'] = True
                    e['isHyphen'] = True

                # print information for debugging and determining the indices for 
                # ignored or added melismas
                if print_syllable_index:
                    print(f'{i}: {e["lyrics"]}')

                # move to the next syllable
                syllable_index = syllable_index+1

        # move to the next word if we've used all syllables in the current word
        if syllable_index > len(words[word_index]) - 1:
            syllable_index = 0
            word_index = word_index+1 

    # save the output
    if output_path.endswith('byz'):
        with zipfile.ZipFile(output_path,'w', compression=zipfile.ZIP_DEFLATED) as z: 
            z.writestr(output_path + 'x', json.dumps(score, indent=2))
    elif output_path.endswith('byzx'):
        with open(output_path, 'w') as f:
            json.dump(score, f, indent=2)
    else:
        raise Exception('Unrecognized extensions for output_path. Expected byz or byzx.')

    print(f'Output saved to {output_path}')

def __is_melisma(e):
    return 'isMelisma' in e and e['isMelisma'] == True

def __get_overrides(lang, overrides):
    if lang in default_overrides:
        return default_overrides[lang] | overrides
    else:
        return overrides


def __preprocess_text(text: str, overrides=dict(), word_overrides_by_index=dict(), print_word_index = False, lang = "en_US"):
    all_overrides = __get_overrides(lang, overrides)

    # remove * and new lines
    sanitized = text.replace('*', ' ').replace('\n', ' ').replace('’', "'")
    
    #split into words
    words = sanitized.split(' ')

    syllables = []

    dic = pyphen.Pyphen(lang=lang)

    # loop over the words and hyphenate
    for i, w in enumerate(words):
        if w != '':
            # print information for debugging and determining the indices for 
            # ignored or added melismas
            if print_word_index:
                print(f'{i}: {w}')

            if i in word_overrides_by_index:
                syllables.append(word_overrides_by_index[i])
                continue

            temp = []

            # save punctuation for later, but remove it for now
            punctuation = ''
            
            if '.' in w or ',' in w or ';' in w or ':' in w:
                punctuation = w[len(w) - 1]
                w = w.replace('.', '').replace(',', '').replace(';', '').replace(':', '')
            elif "'s" in w:
                punctuation = "'s"
                w = w.replace("'s", '')
            elif w.endswith("'"):
                punctuation = "'"
                w = w[:-1]
                

            # split by hyphen in the case of hyphenated words like 'ever-venerable'
            for s in w.split('-'):
                # save capitalization for later, but convert to lower case for now
                capital = False
                if s[0].isupper():
                    capital = True
                    s = s.lower()

                # hyphenate
                hyphenated = all_overrides[s] if s in all_overrides else dic.inserted(s)

                if capital:
                    # restore capitals
                    hyphenated = hyphenated.capitalize()

                temp = temp + hyphenated.split('-')

            # restore punctuation
            if punctuation:
                temp[len(temp) - 1] += punctuation

            syllables.append(temp)

    return syllables