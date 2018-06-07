from scrapy.spiders import CrawlSpider
# from scrapy_splash import SplashRequest
from urllib import parse
import re
from scrapy.selector import Selector
import datetime
import pymongo
from myCrawler.settings import MONGODB_HOST
from myCrawler.settings import MONGODB_PORT
from lxml import etree

nowTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')  # 现在时刻


class diseaseSpider(CrawlSpider):
    name = "diseaseSpider"

    start_urls = [
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Oral disorders&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Tuberculosis&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Sense organ diseases&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Skin and subcutaneous diseases&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Tension-type headache&bytSearchType=0',
        # =================================
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Hemoglobinopathies and hemolytic anemias&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Intestinal nematode infections&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Sexually transmitted diseases excluding HIV&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Acute hepatitis&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Gynecological diseases&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Low back and neck pain&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Migraine&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Diabetes mellitus&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Dietary iron deficiency&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Osteoarthritis&bytSearchType=0',
        # =================================
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Food-borne trematodiases&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Gastritis and duodenitis&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Falls&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Depressive disorders&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Other musculoskeletal disorders&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Chronic obstructive pulmonary disease&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Road injuries&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Anxiety disorders&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Asthma&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Upper respiratory infections&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Interpersonal violence&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Exposure to mechanical forces&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Urinary diseases and male infertility&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Chronic kidney disease&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Other mental and substance use disorders&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Stroke&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Peptic ulcer disease&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Other unintentional injuries&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Ischemic heart disease&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Peripheral artery disease&bytSearchType=0',
        # =================================
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Endocrine, metabolic, blood, and immune disorders&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Idiopathic developmental intellectual disability&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Environmental heat and cold exposure&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Iodine deficiency&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Vitamin A deficiency&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Alcohol use disorders&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Attention-deficit/hyperactivity disorder&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Other cardiovascular and circulatory diseases&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Fire, heat, and hot substances&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Congenital birth defects&bytSearchType=0',
        # =================================
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Otitis media&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Other transport injuries&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Drug use disorders&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Autistic spectrum disorders&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Alzheimer disease and other dementias&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Atrial fibrillation and flutter&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Neonatal preterm birth&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Gout&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Foreign body&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Schizophrenia&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Gallbladder and biliary diseases&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Cirrhosis and other chronic liver diseases due to hepatitis B&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Inguinal, femoral, and abdominal hernia&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Conduct disorder&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Hypertensive heart disease&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Bipolar disorder&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Executions and police conflict&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Encephalitis&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Diarrheal diseases&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Rheumatoid arthritis&bytSearchType=0',
        # =================================
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Animal contact&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Epilepsy&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Cirrhosis and other chronic liver diseases due to other causes&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Inflammatory bowel disease&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Other neglected tropical diseases&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Other unspecified infectious diseases&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Rheumatic heart disease&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Cirrhosis and other chronic liver diseases due to alcohol use&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Varicella and herpes zoster&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Protein-energy malnutrition&bytSearchType=0',
        # =================================
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Cirrhosis and other chronic liver diseases due to hepatitis C&bytSearchType=0',
        # =================================
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Colon and rectum cancer&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Eating disorders&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Parkinson disease&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Breast cancer&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Drowning&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Self-harm&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Interstitial lung disease and pulmonary sarcoidosis&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Schistosomiasis&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Tracheal, bronchus, and lung cancer&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Lower respiratory infections&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Stomach cancer&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Neonatal encephalopathy due to birth asphyxia and trauma&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Pneumoconiosis&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Cardiomyopathy and myocarditis&bytSearchType=0',
        # =================================
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=HIV/AIDS&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Liver cancer&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Other neoplasms&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Cysticercosis&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Exposure to forces of nature&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Poisonings&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Meningitis&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Adverse effects of medical treatment&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Leukemia&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Neonatal sepsis and other neonatal infections&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Prostate cancer&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Cervical cancer&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Uterine cancer&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Trachoma&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Esophageal cancer&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Hemolytic disease and other neonatal jaundice&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Brain and nervous system cancer&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Bladder cancer&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Non-Hodgkin lymphoma&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Maternal hypertensive disorders&bytSearchType=0',
        # =================================
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Thyroid cancer&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Pancreatitis&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Maternal hemorrhage&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Kidney cancer&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Lip and oral cavity cancer&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Nasopharynx cancer&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Dengue&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Larynx cancer&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Multiple sclerosis&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Ovarian cancer&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Conflict and terrorism&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Appendicitis&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Maternal abortion, miscarriage, and ectopic pregnancy&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Pancreatic cancer&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Malignant skin melanoma&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Motor neuron disease&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Multiple myeloma&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Non-melanoma skin cancer&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Endocarditis&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Acute glomerulonephritis&bytSearchType=0',
        # =================================
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Paralytic ileus and intestinal obstruction&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Maternal sepsis and other maternal infections&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Other pharynx cancer&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Hodgkin lymphoma&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Testicular cancer&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Gallbladder and biliary tract cancer&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Cystic echinococcosis&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Leprosy&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Intestinal infectious diseases&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Maternal obstructed labor and uterine rupture&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Vascular intestinal disorders&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Whooping cough&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Tetanus&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Mesothelioma&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Measles&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Other neurological disorders&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Malaria&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Leishmaniasis&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Rabies&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Diphtheria&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Chagas disease&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=African trypanosomiasis&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Lymphatic filariasis&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Onchocerciasis&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Yellow fever&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Indirect maternal deaths&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Late maternal deaths&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Other maternal disorders&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Other neonatal disorders&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Other nutritional deficiencies&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Aortic aneurysm&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Other chronic respiratory diseases&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Other digestive diseases&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Sudden infant death syndrome&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=None&bytSearchType=0',
        'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Maternal deaths aggravated by HIV/AIDS&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Ebola&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Zika virus&bytSearchType=0',
        # 'http://www.diseasesdatabase.com/item_choice.asp?strUserInput=Guinea worm disease&bytSearchType=0'
    ]

    def parse(self, response):
        res_url = response.url
        print('现在进行到: '+res_url)
        # print(response.text)

        selector = Selector(response=response)
        #
        matches_found_list = selector.xpath('//*[@id="page_specific_content"]/strong/a')
        disease_item = {}
        for each_matches_found in matches_found_list:
            disease_item[each_matches_found.xpath('./text()').extract()[0]] = 'http://www.diseasesdatabase.com/'+each_matches_found.xpath('./@href').extract()[0]

        additional_matches_list = selector.xpath('//*[@id="page_specific_content"]/a')
        additional_disease_item = {}
        for each_additional_matches in additional_matches_list:
            additional_disease_item[each_additional_matches.xpath('./text()').extract()[0]] = 'http://www.diseasesdatabase.com/'+each_additional_matches.xpath('./@href').extract()[0]

        search_term = str(selector.xpath('//*[@id="page_specific_content"]/table[1]/tr[2]/td[1]/text()').extract()[0]).strip()

        US_National_Library_of_Medicine = {}
        US_National_Library_of_Medicine['PubMed'] = str(selector.xpath('//*[@id="page_specific_content"]/table[1]/tr[2]/td[2]/a/@href').extract())
        US_National_Library_of_Medicine['PubChem'] = str(selector.xpath('//*[@id="page_specific_content"]/table[1]/tr[2]/td[3]/a/@href').extract())
        US_National_Library_of_Medicine['MedlinePlus'] = str(selector.xpath('//*[@id="page_specific_content"]/table[1]/tr[2]/td[4]/a/@href').extract())
        US_National_Library_of_Medicine['Online Mendelian Inheritance in Man'] = str(selector.xpath('//*[@id="page_specific_content"]/table[1]/tr[2]/td[5]/a/@href').extract())
        US_National_Library_of_Medicine['DailyMed'] = str(selector.xpath('//*[@id="page_specific_content"]/table[1]/tr[2]/td[6]/a/@href').extract())

        Medical_databases = {}
        Medical_databases['MalaCards'] = str(selector.xpath('//*[@id="page_specific_content"]/table[1]/tr[2]/td[8]/a/@href').extract())

        Guidelines = {}
        Guidelines['National Guideline Clearinghouse'] = str(selector.xpath('//*[@id="page_specific_content"]/table[1]/tr[2]/td[9]/a/@href').extract())

        Dictionaries = {}
        Dictionaries['OneLook'] = str(selector.xpath('//*[@id="page_specific_content"]/table[2]/tr[2]/td[2]/a/@href').extract())
        Dictionaries['On-line Medical Dictionary'] = str(selector.xpath('//*[@id="page_specific_content"]/table[2]/tr[2]/td[3]/a/@href').extract())

        Online_textbooks = {}
        Online_textbooks['GP Notebook'] = str(selector.xpath('//*[@id="page_specific_content"]/table[2]/tr[2]/td[4]/a/@href').extract())
        Online_textbooks['MSD (Merck) Manual'] = str(selector.xpath('//*[@id="page_specific_content"]/table[2]/tr[2]/td[5]/a/@href').extract())
        Online_textbooks['Radiopaedia'] = str(selector.xpath('//*[@id="page_specific_content"]/table[2]/tr[2]/td[6]/a/@href').extract())
        Online_textbooks['DailyMed'] = str(selector.xpath('//*[@id="page_specific_content"]/table[2]/tr[2]/td[7]/a/@href').extract())

        Drugs_and_medications = {}
        Drugs_and_medications['DrugBank'] = str(selector.xpath('//*[@id="page_specific_content"]/table[2]/tr[2]/td[8]/a/@href').extract())
        Drugs_and_medications['EMC'] = str(selector.xpath('//*[@id="page_specific_content"]/table[2]/tr[2]/td[9]/a/@href').extract())
        Drugs_and_medications['Bing'] = str(selector.xpath('//*[@id="page_specific_content"]/table[2]/tr[2]/td[10]/a/@href').extract())

        Misc = {}
        Misc['BioMedSearch'] = str(selector.xpath('//*[@id="page_specific_content"]/table[2]/tr[2]/td[11]/a/@href').extract())
        Misc['Google'] = str(selector.xpath('//*[@id="page_specific_content"]/table[2]/tr[2]/td[12]/a/@href').extract())
        Misc['NIH Clinical Trials'] = str(selector.xpath('//*[@id="page_specific_content"]/table[2]/tr[2]/td[13]/a/@href').extract())
        Misc['SNOMED'] =  'http://www.diseasesdatabase.com/'+str(selector.xpath('//*[@id="page_specific_content"]/table[2]/tr[2]/td[14]/a/@href').extract()[0])
        Misc['WikiDoc'] = str(selector.xpath('//*[@id="page_specific_content"]/table[2]/tr[2]/td[15]/a/@href').extract())
        Misc['Wikipedia'] = str(selector.xpath('//*[@id="page_specific_content"]/table[2]/tr[2]/td[16]/a/@href').extract())

        # with open('../crawler_files/disease_webs/' + search_term + '.html', 'w') as f:
        #     f.write(response.text)

        data = {
            'url': res_url,
            'disease': parse.unquote(re.search(r'(strUserInput=)(.*)(&bytSearchType=0)', res_url).group(2)),
            'match_found': disease_item,
            'additional matches': additional_disease_item,
            'Search term': search_term,
            'US National Library of Medicine': US_National_Library_of_Medicine,
            'Medical_databases': Medical_databases,
            'Guidelines': Guidelines,
            'Dictionaries': Dictionaries,
            'Online_textbooks': Online_textbooks,
            'Drugs_and_medications': Drugs_and_medications,
            'Misc': Misc
        }
        # print(data)

        connection = pymongo.MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
        tdb = connection.disease
        post_info = tdb.disease_database
        post_info.insert(data)