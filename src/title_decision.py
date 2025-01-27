#MIT License

#Copyright (c) 2018 The University of Michigan

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

from supervised_classifier_ngram import supervised_classifier_ngram
from supervised_classifier import supervised_classifier
from pdf_to_text import pdf_to_text
from pdf_cropper_title import pdf_cropper_title
from key_words_title_counter import key_words_title_counter
from title_arbitration import title_arbitration
from Address import Address
import os
def title_decision():
    Path_extracted=Address(1).split("\n")
    Path_extracted1=Path_extracted[0]
    ADC = 'ADC'
    BDRT = 'BDRT'
    CDC = 'CDC'
    counters = 'counters'
    DAC = 'DAC'
    DCDC = 'DCDC'
    Delay_Line = 'Delay_Line'
    DSP = 'DSP'
    IO = 'IO'
    LDO = 'LDO'
    Opamp = 'Opamp'
    Digital_Potentiometers = 'Digital_Potentiometers'
    PLL = 'PLL'
    SRAM = 'SRAM'
    Temperature_Sensor = 'Temperature_Sensor'

    ADC_path = [os.path.join(os.path.join(Path_extracted1, 'cropped_text'), 'ADC'), ADC]
    BDRT_path = [os.path.join(os.path.join(Path_extracted1, 'cropped_text'), 'BDRT'), BDRT]
    CDC_path = [os.path.join(os.path.join(Path_extracted1, 'cropped_text'), 'CDC'), CDC]
    COUNTER_path = [os.path.join(os.path.join(Path_extracted1, 'cropped_text'), 'counters'), counters]
    DAC_path = [os.path.join(os.path.join(Path_extracted1, 'cropped_text'), 'DAC'), DAC]
    DCDC_path = [os.path.join(os.path.join(Path_extracted1, 'cropped_text'), 'DCDC'), DCDC]
    DELAY_LINE_path = [os.path.join(os.path.join(Path_extracted1, 'cropped_text'), 'Delay_Line'), Delay_Line]
    DSP_path = [os.path.join(os.path.join(Path_extracted1, 'cropped_text'), 'DSP'), DSP]
    IO_path = [os.path.join(os.path.join(Path_extracted1, 'cropped_text'), 'IO'), IO]
    LDO_path = [os.path.join(os.path.join(Path_extracted1, 'cropped_text'), 'LDO'), LDO]
    OPAMP_path = [os.path.join(os.path.join(Path_extracted1, 'cropped_text'), 'Opamp'), Opamp]
    POTENTIOMETER_path = [os.path.join(os.path.join(Path_extracted1, 'cropped_text'), 'Digital_Potentiometers'), Digital_Potentiometers]
    PLL_path = [os.path.join(os.path.join(Path_extracted1, 'cropped_text'), 'PLL'), PLL]
    SRAM_path = [os.path.join(os.path.join(Path_extracted1, 'cropped_text'), 'SRAM'), SRAM]
    Temperature_Sensor_path = [os.path.join(os.path.join(Path_extracted1, 'cropped_text'), 'Temperature_Sensor'),Temperature_Sensor]

    SOURCES = [ADC_path,BDRT_path,COUNTER_path,DAC_path,DELAY_LINE_path,DSP_path,IO_path,OPAMP_path,POTENTIOMETER_path,PLL_path,DCDC_path,CDC_path,Temperature_Sensor_path,SRAM_path,LDO_path]
    previous_Test_text_dir=os.path.join(Path_extracted1,'Test_text')
    previous_cropped_pdf_dir=os.path.join(Path_extracted1,'Test_cropped_pdf')
    previous_cropped_text_dir=os.path.join(Path_extracted1,'Test_cropped_text')
    for file in os.listdir(previous_Test_text_dir):
        os.remove(os.path.join(previous_Test_text_dir,file))
    for file in os.listdir(previous_cropped_pdf_dir):
        os.remove(os.path.join(previous_cropped_pdf_dir,file))
    for file in os.listdir(previous_cropped_text_dir):
        os.remove(os.path.join(previous_cropped_text_dir,file))
        
    pdf_to_text('Test_pdf','Test_text')
    pdf_cropper_title('Test_pdf','Test_cropped_pdf')
    pdf_to_text('Test_cropped_pdf','Test_cropped_text')
    normal_classifier_title_result=supervised_classifier(SOURCES)
    #ngram_classifier_title_result=supervised_classifier_ngram(SOURCES)
    #print(normal_classifier_title_result)
    #print(ngram_classifier_title_result)
    [key_words_title_result,key_words_occurrence_array,key_words_title_result_second,max_zero_flag,max_second_zero_flag]=key_words_title_counter('Test_text')
    title=title_arbitration(normal_classifier_title_result,key_words_title_result,key_words_occurrence_array,key_words_title_result_second,max_zero_flag,max_second_zero_flag)
    #print(key_words_title_result,key_words_occurrence_array)
    #print(key_words_title_result)
    #print(key_words_title_result_second)
    #print(title)
    titles=[]
    for elem in title:
        titles.append(elem)
    return titles
