# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CSV_Manager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('uri', models.CharField(max_length=1000, blank=True)),
                ('title', models.CharField(max_length=255, blank=True)),
                ('description', models.TextField(blank=True)),
                ('file', models.FileField(upload_to='/var/opensemanticsearch/csv', blank=True)),
                ('codec', models.CharField(max_length=255, help_text='Which encoding? (Leave blank for systems default, try modern and international utf-8 or for older german format iso-8859-15)', choices=[('037', '037'), ('1026', '1026'), ('1125', '1125'), ('1140', '1140'), ('1250', '1250'), ('1251', '1251'), ('1252', '1252'), ('1253', '1253'), ('1254', '1254'), ('1255', '1255'), ('1256', '1256'), ('1257', '1257'), ('1258', '1258'), ('273', '273'), ('424', '424'), ('437', '437'), ('500', '500'), ('646', '646'), ('775', '775'), ('850', '850'), ('852', '852'), ('855', '855'), ('857', '857'), ('858', '858'), ('860', '860'), ('861', '861'), ('862', '862'), ('863', '863'), ('864', '864'), ('865', '865'), ('866', '866'), ('869', '869'), ('8859', '8859'), ('932', '932'), ('936', '936'), ('949', '949'), ('950', '950'), ('ansi_x3.4_1968', 'ansi_x3.4_1968'), ('ansi_x3.4_1986', 'ansi_x3.4_1986'), ('ansi_x3_4_1968', 'ansi_x3_4_1968'), ('arabic', 'arabic'), ('ascii', 'ascii'), ('asmo_708', 'asmo_708'), ('base64', 'base64'), ('base64_codec', 'base64_codec'), ('base_64', 'base_64'), ('big5', 'big5'), ('big5_hkscs', 'big5_hkscs'), ('big5_tw', 'big5_tw'), ('big5hkscs', 'big5hkscs'), ('bz2', 'bz2'), ('bz2_codec', 'bz2_codec'), ('chinese', 'chinese'), ('cp037', 'cp037'), ('cp1026', 'cp1026'), ('cp1125', 'cp1125'), ('cp1140', 'cp1140'), ('cp1250', 'cp1250'), ('cp1251', 'cp1251'), ('cp1252', 'cp1252'), ('cp1253', 'cp1253'), ('cp1254', 'cp1254'), ('cp1255', 'cp1255'), ('cp1256', 'cp1256'), ('cp1257', 'cp1257'), ('cp1258', 'cp1258'), ('cp1361', 'cp1361'), ('cp154', 'cp154'), ('cp273', 'cp273'), ('cp367', 'cp367'), ('cp424', 'cp424'), ('cp437', 'cp437'), ('cp500', 'cp500'), ('cp775', 'cp775'), ('cp819', 'cp819'), ('cp850', 'cp850'), ('cp852', 'cp852'), ('cp855', 'cp855'), ('cp857', 'cp857'), ('cp858', 'cp858'), ('cp860', 'cp860'), ('cp861', 'cp861'), ('cp862', 'cp862'), ('cp863', 'cp863'), ('cp864', 'cp864'), ('cp865', 'cp865'), ('cp866', 'cp866'), ('cp866u', 'cp866u'), ('cp869', 'cp869'), ('cp932', 'cp932'), ('cp936', 'cp936'), ('cp949', 'cp949'), ('cp950', 'cp950'), ('cp_gr', 'cp_gr'), ('cp_is', 'cp_is'), ('csHPRoman8', 'csHPRoman8'), ('csascii', 'csascii'), ('csbig5', 'csbig5'), ('csibm037', 'csibm037'), ('csibm1026', 'csibm1026'), ('csibm273', 'csibm273'), ('csibm424', 'csibm424'), ('csibm500', 'csibm500'), ('csibm855', 'csibm855'), ('csibm857', 'csibm857'), ('csibm858', 'csibm858'), ('csibm860', 'csibm860'), ('csibm861', 'csibm861'), ('csibm863', 'csibm863'), ('csibm864', 'csibm864'), ('csibm865', 'csibm865'), ('csibm866', 'csibm866'), ('csibm869', 'csibm869'), ('csiso2022jp', 'csiso2022jp'), ('csiso2022kr', 'csiso2022kr'), ('csiso58gb231280', 'csiso58gb231280'), ('csisolatin1', 'csisolatin1'), ('csisolatin2', 'csisolatin2'), ('csisolatin3', 'csisolatin3'), ('csisolatin4', 'csisolatin4'), ('csisolatin5', 'csisolatin5'), ('csisolatin6', 'csisolatin6'), ('csisolatinarabic', 'csisolatinarabic'), ('csisolatincyrillic', 'csisolatincyrillic'), ('csisolatingreek', 'csisolatingreek'), ('csisolatinhebrew', 'csisolatinhebrew'), ('cskoi8r', 'cskoi8r'), ('cspc775baltic', 'cspc775baltic'), ('cspc850multilingual', 'cspc850multilingual'), ('cspc862latinhebrew', 'cspc862latinhebrew'), ('cspc8codepage437', 'cspc8codepage437'), ('cspcp852', 'cspcp852'), ('csptcp154', 'csptcp154'), ('csshiftjis', 'csshiftjis'), ('cyrillic', 'cyrillic'), ('cyrillic_asian', 'cyrillic_asian'), ('dbcs', 'dbcs'), ('ebcdic_cp_be', 'ebcdic_cp_be'), ('ebcdic_cp_ca', 'ebcdic_cp_ca'), ('ebcdic_cp_ch', 'ebcdic_cp_ch'), ('ebcdic_cp_he', 'ebcdic_cp_he'), ('ebcdic_cp_nl', 'ebcdic_cp_nl'), ('ebcdic_cp_us', 'ebcdic_cp_us'), ('ebcdic_cp_wt', 'ebcdic_cp_wt'), ('ecma_114', 'ecma_114'), ('ecma_118', 'ecma_118'), ('elot_928', 'elot_928'), ('euc_cn', 'euc_cn'), ('euc_jis2004', 'euc_jis2004'), ('euc_jis_2004', 'euc_jis_2004'), ('euc_jisx0213', 'euc_jisx0213'), ('euc_jp', 'euc_jp'), ('euc_kr', 'euc_kr'), ('euccn', 'euccn'), ('eucgb2312_cn', 'eucgb2312_cn'), ('eucjis2004', 'eucjis2004'), ('eucjisx0213', 'eucjisx0213'), ('eucjp', 'eucjp'), ('euckr', 'euckr'), ('gb18030', 'gb18030'), ('gb18030_2000', 'gb18030_2000'), ('gb2312', 'gb2312'), ('gb2312_1980', 'gb2312_1980'), ('gb2312_80', 'gb2312_80'), ('gbk', 'gbk'), ('greek', 'greek'), ('greek8', 'greek8'), ('hebrew', 'hebrew'), ('hex', 'hex'), ('hex_codec', 'hex_codec'), ('hkscs', 'hkscs'), ('hp_roman8', 'hp_roman8'), ('hz', 'hz'), ('hz_gb', 'hz_gb'), ('hz_gb_2312', 'hz_gb_2312'), ('hzgb', 'hzgb'), ('ibm037', 'ibm037'), ('ibm039', 'ibm039'), ('ibm1026', 'ibm1026'), ('ibm1125', 'ibm1125'), ('ibm1140', 'ibm1140'), ('ibm273', 'ibm273'), ('ibm367', 'ibm367'), ('ibm424', 'ibm424'), ('ibm437', 'ibm437'), ('ibm500', 'ibm500'), ('ibm775', 'ibm775'), ('ibm819', 'ibm819'), ('ibm850', 'ibm850'), ('ibm852', 'ibm852'), ('ibm855', 'ibm855'), ('ibm857', 'ibm857'), ('ibm858', 'ibm858'), ('ibm860', 'ibm860'), ('ibm861', 'ibm861'), ('ibm862', 'ibm862'), ('ibm863', 'ibm863'), ('ibm864', 'ibm864'), ('ibm865', 'ibm865'), ('ibm866', 'ibm866'), ('ibm869', 'ibm869'), ('iso2022_jp', 'iso2022_jp'), ('iso2022_jp_1', 'iso2022_jp_1'), ('iso2022_jp_2', 'iso2022_jp_2'), ('iso2022_jp_2004', 'iso2022_jp_2004'), ('iso2022_jp_3', 'iso2022_jp_3'), ('iso2022_jp_ext', 'iso2022_jp_ext'), ('iso2022_kr', 'iso2022_kr'), ('iso2022jp', 'iso2022jp'), ('iso2022jp_1', 'iso2022jp_1'), ('iso2022jp_2', 'iso2022jp_2'), ('iso2022jp_2004', 'iso2022jp_2004'), ('iso2022jp_3', 'iso2022jp_3'), ('iso2022jp_ext', 'iso2022jp_ext'), ('iso2022kr', 'iso2022kr'), ('iso646_us', 'iso646_us'), ('iso8859', 'iso8859'), ('iso8859_1', 'iso8859_1'), ('iso8859_10', 'iso8859_10'), ('iso8859_11', 'iso8859_11'), ('iso8859_13', 'iso8859_13'), ('iso8859_14', 'iso8859_14'), ('iso8859_15', 'iso8859_15'), ('iso8859_16', 'iso8859_16'), ('iso8859_2', 'iso8859_2'), ('iso8859_3', 'iso8859_3'), ('iso8859_4', 'iso8859_4'), ('iso8859_5', 'iso8859_5'), ('iso8859_6', 'iso8859_6'), ('iso8859_7', 'iso8859_7'), ('iso8859_8', 'iso8859_8'), ('iso8859_9', 'iso8859_9'), ('iso_2022_jp', 'iso_2022_jp'), ('iso_2022_jp_1', 'iso_2022_jp_1'), ('iso_2022_jp_2', 'iso_2022_jp_2'), ('iso_2022_jp_2004', 'iso_2022_jp_2004'), ('iso_2022_jp_3', 'iso_2022_jp_3'), ('iso_2022_jp_ext', 'iso_2022_jp_ext'), ('iso_2022_kr', 'iso_2022_kr'), ('iso_646.irv_1991', 'iso_646.irv_1991'), ('iso_8859_1', 'iso_8859_1'), ('iso_8859_10', 'iso_8859_10'), ('iso_8859_10_1992', 'iso_8859_10_1992'), ('iso_8859_11', 'iso_8859_11'), ('iso_8859_11_2001', 'iso_8859_11_2001'), ('iso_8859_13', 'iso_8859_13'), ('iso_8859_14', 'iso_8859_14'), ('iso_8859_14_1998', 'iso_8859_14_1998'), ('iso_8859_15', 'iso_8859_15'), ('iso_8859_16', 'iso_8859_16'), ('iso_8859_16_2001', 'iso_8859_16_2001'), ('iso_8859_1_1987', 'iso_8859_1_1987'), ('iso_8859_2', 'iso_8859_2'), ('iso_8859_2_1987', 'iso_8859_2_1987'), ('iso_8859_3', 'iso_8859_3'), ('iso_8859_3_1988', 'iso_8859_3_1988'), ('iso_8859_4', 'iso_8859_4'), ('iso_8859_4_1988', 'iso_8859_4_1988'), ('iso_8859_5', 'iso_8859_5'), ('iso_8859_5_1988', 'iso_8859_5_1988'), ('iso_8859_6', 'iso_8859_6'), ('iso_8859_6_1987', 'iso_8859_6_1987'), ('iso_8859_7', 'iso_8859_7'), ('iso_8859_7_1987', 'iso_8859_7_1987'), ('iso_8859_8', 'iso_8859_8'), ('iso_8859_8_1988', 'iso_8859_8_1988'), ('iso_8859_9', 'iso_8859_9'), ('iso_8859_9_1989', 'iso_8859_9_1989'), ('iso_celtic', 'iso_celtic'), ('iso_ir_100', 'iso_ir_100'), ('iso_ir_101', 'iso_ir_101'), ('iso_ir_109', 'iso_ir_109'), ('iso_ir_110', 'iso_ir_110'), ('iso_ir_126', 'iso_ir_126'), ('iso_ir_127', 'iso_ir_127'), ('iso_ir_138', 'iso_ir_138'), ('iso_ir_144', 'iso_ir_144'), ('iso_ir_148', 'iso_ir_148'), ('iso_ir_157', 'iso_ir_157'), ('iso_ir_166', 'iso_ir_166'), ('iso_ir_199', 'iso_ir_199'), ('iso_ir_226', 'iso_ir_226'), ('iso_ir_58', 'iso_ir_58'), ('iso_ir_6', 'iso_ir_6'), ('jisx0213', 'jisx0213'), ('johab', 'johab'), ('koi8_r', 'koi8_r'), ('korean', 'korean'), ('ks_c_5601', 'ks_c_5601'), ('ks_c_5601_1987', 'ks_c_5601_1987'), ('ks_x_1001', 'ks_x_1001'), ('ksc5601', 'ksc5601'), ('ksx1001', 'ksx1001'), ('kz1048', 'kz1048'), ('kz_1048', 'kz_1048'), ('l1', 'l1'), ('l10', 'l10'), ('l2', 'l2'), ('l3', 'l3'), ('l4', 'l4'), ('l5', 'l5'), ('l6', 'l6'), ('l7', 'l7'), ('l8', 'l8'), ('l9', 'l9'), ('latin', 'latin'), ('latin1', 'latin1'), ('latin10', 'latin10'), ('latin2', 'latin2'), ('latin3', 'latin3'), ('latin4', 'latin4'), ('latin5', 'latin5'), ('latin6', 'latin6'), ('latin7', 'latin7'), ('latin8', 'latin8'), ('latin9', 'latin9'), ('latin_1', 'latin_1'), ('mac_cyrillic', 'mac_cyrillic'), ('mac_greek', 'mac_greek'), ('mac_iceland', 'mac_iceland'), ('mac_latin2', 'mac_latin2'), ('mac_roman', 'mac_roman'), ('mac_turkish', 'mac_turkish'), ('maccentraleurope', 'maccentraleurope'), ('maccyrillic', 'maccyrillic'), ('macgreek', 'macgreek'), ('maciceland', 'maciceland'), ('macintosh', 'macintosh'), ('maclatin2', 'maclatin2'), ('macroman', 'macroman'), ('macturkish', 'macturkish'), ('mbcs', 'mbcs'), ('ms1361', 'ms1361'), ('ms932', 'ms932'), ('ms936', 'ms936'), ('ms949', 'ms949'), ('ms950', 'ms950'), ('ms_kanji', 'ms_kanji'), ('mskanji', 'mskanji'), ('pt154', 'pt154'), ('ptcp154', 'ptcp154'), ('quopri', 'quopri'), ('quopri_codec', 'quopri_codec'), ('quoted_printable', 'quoted_printable'), ('quotedprintable', 'quotedprintable'), ('r8', 'r8'), ('rk1048', 'rk1048'), ('roman8', 'roman8'), ('rot13', 'rot13'), ('rot_13', 'rot_13'), ('ruscii', 'ruscii'), ('s_jis', 's_jis'), ('s_jis_2004', 's_jis_2004'), ('s_jisx0213', 's_jisx0213'), ('shift_jis', 'shift_jis'), ('shift_jis_2004', 'shift_jis_2004'), ('shift_jisx0213', 'shift_jisx0213'), ('shiftjis', 'shiftjis'), ('shiftjis2004', 'shiftjis2004'), ('shiftjisx0213', 'shiftjisx0213'), ('sjis', 'sjis'), ('sjis_2004', 'sjis_2004'), ('sjisx0213', 'sjisx0213'), ('strk1048_2002', 'strk1048_2002'), ('tactis', 'tactis'), ('thai', 'thai'), ('tis260', 'tis260'), ('tis620', 'tis620'), ('tis_620', 'tis_620'), ('tis_620_0', 'tis_620_0'), ('tis_620_2529_0', 'tis_620_2529_0'), ('tis_620_2529_1', 'tis_620_2529_1'), ('u16', 'u16'), ('u32', 'u32'), ('u7', 'u7'), ('u8', 'u8'), ('u_jis', 'u_jis'), ('uhc', 'uhc'), ('ujis', 'ujis'), ('unicode_1_1_utf_7', 'unicode_1_1_utf_7'), ('unicodebigunmarked', 'unicodebigunmarked'), ('unicodelittleunmarked', 'unicodelittleunmarked'), ('us', 'us'), ('us_ascii', 'us_ascii'), ('utf', 'utf'), ('utf16', 'utf16'), ('utf32', 'utf32'), ('utf7', 'utf7'), ('utf8', 'utf8'), ('utf8_ucs2', 'utf8_ucs2'), ('utf8_ucs4', 'utf8_ucs4'), ('utf_16', 'utf_16'), ('utf_16_be', 'utf_16_be'), ('utf_16_le', 'utf_16_le'), ('utf_16be', 'utf_16be'), ('utf_16le', 'utf_16le'), ('utf_32', 'utf_32'), ('utf_32_be', 'utf_32_be'), ('utf_32_le', 'utf_32_le'), ('utf_32be', 'utf_32be'), ('utf_32le', 'utf_32le'), ('utf_7', 'utf_7'), ('utf_8', 'utf_8'), ('uu', 'uu'), ('uu_codec', 'uu_codec'), ('windows_1250', 'windows_1250'), ('windows_1251', 'windows_1251'), ('windows_1252', 'windows_1252'), ('windows_1253', 'windows_1253'), ('windows_1254', 'windows_1254'), ('windows_1255', 'windows_1255'), ('windows_1256', 'windows_1256'), ('windows_1257', 'windows_1257'), ('windows_1258', 'windows_1258'), ('x_mac_japanese', 'x_mac_japanese'), ('x_mac_korean', 'x_mac_korean'), ('x_mac_simp_chinese', 'x_mac_simp_chinese'), ('x_mac_trad_chinese', 'x_mac_trad_chinese'), ('zip', 'zip'), ('zlib', 'zlib'), ('zlib_codec', 'zlib_codec')], blank=True)),
                ('sniff_encoding', models.BooleanField(default=True)),
                ('sniff_dialect', models.BooleanField(default=False)),
                ('delimiter_is_tab', models.BooleanField()),
                ('delimiter', models.CharField(max_length=1, help_text='Leave blank for default , or change to ; or another delimiter char', blank=True)),
                ('quotechar', models.CharField(max_length=1, blank=True)),
                ('doublequote', models.BooleanField()),
                ('escapechar', models.CharField(max_length=1, blank=True)),
                ('title_row', models.IntegerField(null=True, help_text='Row with column titles. Leave blank if the CSV containes only data and no title row', blank=True)),
                ('start_row', models.IntegerField(null=True, help_text='Row where to start. Leave blank or set to 1 if all rows are data', blank=True)),
                ('rows', models.TextField(blank=True)),
                ('rows_include', models.BooleanField(default=False)),
                ('cols', models.TextField(blank=True)),
                ('cols_include', models.BooleanField(default=False)),
            ],
        ),
    ]
