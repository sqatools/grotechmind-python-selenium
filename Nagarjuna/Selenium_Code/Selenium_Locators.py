# i)   //tagname[@attribute='value']
#            //input[@name='fromcity']
#            //input[@id='fromcity']
#            //input[@fdprocessedid='avj1c4']
#
#       ii) //*[@attribute='value']
#           //*[@fdprocessedid='avj1c4']
#
#      iii) multiple element with same attribute : (//tagname[@attribute='value'])[1]
#           (//input[@name='firstname'])[2]

"""
xpath :

1). Absolute XPATH:
/html/body/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/ul/li[5]/a

2). Relative XPATH:
      i)   //tagname[@attribute='value']
           //input[@name='fromcity']
           //input[@id='fromcity']
           //input[@fdprocessedid='avj1c4']

      ii) //*[@attribute='value']
          //*[@fdprocessedid='avj1c4']

     iii) multiple element with same attribute : (//tagname[@attribute='value'])[1]
          (//input[@name='firstname'])[2]

    XPATH Methods:

    1) Text method.  :  //tagname[text()='text value']
                        //h1[text()=' Dummy Ticket Booking Website']
                        //span[text()='Hotels']
                        //span[text()='Dummy ticket for visa application - $200 ']
                        //a[text()='Pytest Framework']
                        //*[text()='Pytest Framework']

    2) Contains Method :
                     //tagname[contains(text(), "partial text value")]
                     //a[contains(text(), 'Pytest')]
                     //h1[contains(text(), 'Dummy')]
                     //span[text()='SEARCH FLIGHTS']


                     //tagname[contains(@attribute, 'partial attribute value')]
                     //*[contains(@id, 'from')]
                     //input[contains(@fdprocessedid,'3c96zt')]

    3) AND & OR
               //tagname[@attribute1 ='value' and @attribute2 = 'value']
               //input[@name='fromcity' and @id='fromcity']
               //input[@name='firstname' and @id='firstname' and @fdprocessedid="2xcfae"]

               //tagname[@attribute1 ='value' or @attribute2 = 'value']
               //input[@name='firstname' or @id='fromcity']

    # Advance Methods in XPATH

    1) Following:
                //tagname[@attrib='value']//following::tagname[@attribute='value']
                //input[@value='radio_345']//following::input[@id='male']

    2) Following-sibling:
                //tagname[@attrib='value']//following-sibling::tagname[@attribute='value']
                //span[text()='From']//following-sibling::p[text()='Enter city or airport']
                //tr[@bgcolor="lightgrey"][2]//following-sibling::tr/td[text()='Kolkata']
    3) parent:
              //tagname[@child_Attrib='value']//parent::tagname[@parent_atrribute='value']
              //td[text()='Indore']//parent::tr
              //td[text()='Kolkata']//parent::tr//following-sibling::tr//td[text()='Delhi']
              //span[text()='Cabs']//parent::a

    4) Ancestor :
            //tagname[@child_Attrib='value']//ancestor::tagname[@parent_atrribute='value']

    5). Preceding:
            //tagname[@child_Attrib='value']//ancestor::tagname[@parent_atrribute='value']
            //input[@id='male']//preceding::input

"""
