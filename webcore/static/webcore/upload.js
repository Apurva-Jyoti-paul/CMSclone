var obj;
var myWidget = cloudinary.createUploadWidget({
  cloudName: 'paulserver', 
  uploadPreset: 'qjwb2yvf'}, (error, result) => { 
    if (!error && result && result.event === "success") { 
      console.log('Done! Here is the image info: ', result.info); 
      console.log(1);
      document.getElementById("ip1").value=result.info.secure_url;
      document.getElementById("ip2").value=result.info.resource_type;
      console.log(document.getElementById("ip1").value);
      document.getElementById("saveform").submit();
    }
  }
)



document.getElementById("upload_widget").addEventListener("click", function(){
    myWidget.open();
  }, false);