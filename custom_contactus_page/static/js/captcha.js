console.log('captcha.js file loaded')
var onloadCallback = function() {
	hcaptcha.render('hcaptcha', {
    'sitekey' : '5999a393-bb2f-40b8-9f06-c952dcbc4089'
  });
};

onloadCallback();

$(document).on('click','#submit',function(){
    var response = hcaptcha.getResponse();
    if (response.length == 0)
    {
        alert('Please fill a captcha');
        return false;
    }
    else{
 
        alert('successfully submitted');       
    
    }
})
