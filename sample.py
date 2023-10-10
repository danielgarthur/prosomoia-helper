import prosomoiahelper

text = """This is my metered text * that I copied * from the liturgical notes * provided
   by my Archdiocese."""

overrides = dict()
overrides['archdiocese'] = 'arch-di-o-cese'
overrides['copied'] = 'cop-ied'
overrides['liturgical'] = 'lit-ur-gic-al'

prosomoiahelper.generate_prosomoia(
    text, 
    'automela.byz', 
    'prosomia.byz',
    overrides)