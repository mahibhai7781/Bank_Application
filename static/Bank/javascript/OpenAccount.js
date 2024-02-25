
function sub()
{
    if(cname.value=='')
    {
        document.getElementById('cnm').innerHTML='This Field is required'
        
    }  
    if(fname.value=='') 
    {
        document.getElementById('fnm').innerHTML='This Field is required'    
    } 
    if(address.value=='')
    {
        document.getElementById('addr').innerHTML='This Field is required'
        
    }  
    if(city.value=='') 
    {
        document.getElementById('ct').innerHTML='This Field is required'    
    }
    if(state.value=='')
    {
        document.getElementById('st').innerHTML='This Field is required'
        
    }  
    if(pin.value=='') 
    {
        document.getElementById('pn').innerHTML='This Field is required'    
    }
    if(mobile.value=='')
    {
        document.getElementById('mb').innerHTML='This Field is required'
        
    }  
    if(dob.value=='') 
    {
        document.getElementById('db').innerHTML='This Field is required'    
    }
    if(religion.value=='')
    {
        document.getElementById('rljn').innerHTML='This Field is required'
        
    }  
    if(gender.value=='') 
    {
        document.getElementById('gen').innerHTML='This Field is required'    
    }
    if(amount.value=='') 
    {
        document.getElementById('amt').innerHTML='This Field is required'    
    }
    else{
        if(Number(amount.value)<=1000)
            document.getElementById('amt').innerHTML='Amount should be minimum 1000 '
            amount.value=''
            amount.focus();
            
        }

    }
    


function Withdraw()
{
    if(account.value=='') 
    {
        document.getElementById('ac').innerHTML='This Field is required'    
    }
    if(amount.value=='') 
    {
        document.getElementById('amt').innerHTML='This Field is required'    
    }
   
}

function Deposit()
{
    if(account.value=='') 
    {
        document.getElementById('ac').innerHTML='This Field is required'    
    }
    if(amount.value=='') 
    {
        document.getElementById('amt').innerHTML='This Field is required'    
    }
   
}


