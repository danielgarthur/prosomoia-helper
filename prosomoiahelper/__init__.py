import json
import pyphen
import zipfile

default_overrides__en_US = dict()

# Names
default_overrides__en_US['apollinarius'] = 'a-pol-lin-ar-i-us'
default_overrides__en_US['arius'] = 'ar-i-us'
default_overrides__en_US['averkios'] = 'a-ver-ki-os'
default_overrides__en_US['cleopas'] = 'cle-o-pas'
default_overrides__en_US['dioscorus'] = 'di-o-scor-us'
default_overrides__en_US['elisseus'] = 'el-is-se-us'
default_overrides__en_US['emmaus'] = 'em-ma-us'
default_overrides__en_US['germanos'] = 'ger-man-os'
default_overrides__en_US['japheth'] = 'japh-eth'
default_overrides__en_US['macedonius'] = 'mac-e-don-i-us'
default_overrides__en_US['nestorius'] = 'nes-tor-i-us'
default_overrides__en_US['pelagia'] = 'pel-a-gi-a'
default_overrides__en_US['sabellius'] = 'sab-el-li-us'
default_overrides__en_US["sev'rus"] = "sev'-rus"
default_overrides__en_US['sion'] = 'si-on'

default_overrides__en_US['abode'] = 'a-bode'
default_overrides__en_US['added'] = 'add-ed'
default_overrides__en_US['aforetime'] = 'a-fore-time'
default_overrides__en_US['alabaster'] = 'al-a-bas-ter'
default_overrides__en_US['again'] = 'a-gain'
default_overrides__en_US['alone'] = 'a-lone'
default_overrides__en_US['anew'] = 'a-new'
default_overrides__en_US['apart'] = 'a-part'
default_overrides__en_US['apostle'] = 'a-pos-tle'
default_overrides__en_US['apostles'] = 'a-pos-tles'
default_overrides__en_US['arising'] = 'a-ris-ing'
default_overrides__en_US['asleep'] = 'a-sleep'
default_overrides__en_US['beheldest'] = 'be-held-est'
default_overrides__en_US['blessed'] = 'bless-ed'
default_overrides__en_US['body'] = 'bod-y'
default_overrides__en_US['canon'] = 'can-on'
default_overrides__en_US['comforter'] = 'com-fort-er'
default_overrides__en_US['covenant'] = 'cov-en-ant'
default_overrides__en_US['creator'] = 'cre-a-tor'
default_overrides__en_US['demons'] = 'de-mons'
default_overrides__en_US['deeply'] = 'deep-ly'
default_overrides__en_US['diseases'] = 'dis-eas-es'
default_overrides__en_US['earnestly'] = 'earn-est-ly'
default_overrides__en_US['entreaties'] = 'en-treat-ies'
default_overrides__en_US['equal'] = 'e-qual'
default_overrides__en_US['even'] = 'ev-en'
default_overrides__en_US['fashioner'] = 'fash-ion-er'
default_overrides__en_US['fiery'] = 'fier-y'
default_overrides__en_US['fragrancy'] = 'fra-gran-cy'
default_overrides__en_US['fulfiller'] = 'ful-fill-er'
default_overrides__en_US['heldest'] = 'held-est'
default_overrides__en_US['heretics'] = 'her-i-tics'
default_overrides__en_US['giveth'] = 'giv-eth'
default_overrides__en_US['gospel'] = 'gos-pel'
default_overrides__en_US['guardeth'] = 'guard-eth'
default_overrides__en_US['greater'] = 'great-er'
default_overrides__en_US['healest'] = 'heal-est'
default_overrides__en_US['holy'] = 'ho-ly'
default_overrides__en_US["hon'rable"] = "hon'-ra-ble"
default_overrides__en_US['illumineth'] = 'il-lum-in-eth'
default_overrides__en_US['inscriber'] = 'in-scrib-er'
default_overrides__en_US['knoweth'] = 'know-eth'
default_overrides__en_US['luminary'] = 'lum-in-ar-y'
default_overrides__en_US['madest'] = 'ma-dest'
default_overrides__en_US['maladies'] = 'mal-a-dies'
default_overrides__en_US['many'] = 'man-y'
default_overrides__en_US['marvelous'] = 'mar-vel-ous'
default_overrides__en_US['mysticly'] = 'mys-tic-ly'
default_overrides__en_US['mystery'] = 'mys-ter-y'
default_overrides__en_US['naked'] = 'na-ked'
default_overrides__en_US['nakedness'] = 'na-ked-ness'
default_overrides__en_US['noetic'] = 'no-et-ic'
default_overrides__en_US['nobly'] = 'nob-ly'
default_overrides__en_US['obedience'] = 'o-be-di-ence'
default_overrides__en_US['odor'] = 'od-or'
default_overrides__en_US['orthodoxy'] = 'or-tho-dox-y'
default_overrides__en_US['overcame'] = 'o-ver-came'
default_overrides__en_US['paradise'] = 'par-a-dise'
default_overrides__en_US['physician'] = 'phys-i-cian'
default_overrides__en_US['piety'] = 'pi-e-ty'
default_overrides__en_US['prophet'] = 'proph-et'
default_overrides__en_US['putting'] = 'put-ting'
default_overrides__en_US["quick'ning"] = "quick'-ning"
default_overrides__en_US['raineth'] = 'rain-eth'
default_overrides__en_US['rather'] = 'rath-er'
default_overrides__en_US['record'] = 'rec-ord'
default_overrides__en_US['recorded'] = 're-cord-ed'
default_overrides__en_US['recorder'] = 're-cord-er'
default_overrides__en_US['revered'] = 'rev-ered'
default_overrides__en_US["rev'rence"] = "rev'-rence"
default_overrides__en_US["sep'rately"] = "sep'-rate-ly"
default_overrides__en_US["sov'reign"] = "sov'-reign"
default_overrides__en_US['sundry'] = "sun-dry"
default_overrides__en_US['tabernacle'] = "tab-er-na-cle"
default_overrides__en_US['tablets'] = "tab-lets"
default_overrides__en_US['taughtest'] = "taught-est"
default_overrides__en_US["temp'rance"] = "temp'-rance"
default_overrides__en_US["temp'rance"] = "temp'-rance"
default_overrides__en_US['thereafter'] = "there-af-ter"
default_overrides__en_US['treasury'] = "trea-sur-y"
default_overrides__en_US["tyrant"] = "ty-rant"
default_overrides__en_US['unaware'] = 'un-a-ware'
default_overrides__en_US['unerring'] = 'un-err-ing'
default_overrides__en_US['universe'] = 'u-ni-verse'
default_overrides__en_US["ven'rable"] = "ven'-ra-ble"
default_overrides__en_US['virtue'] = 'vir-tue'

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