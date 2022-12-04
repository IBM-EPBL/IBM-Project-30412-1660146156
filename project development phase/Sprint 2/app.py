<!DOCTYPE html>
<html lang="en">

<head>
  <title>Request</title>
  <script>
    window.watsonAssistantChatOptions = {
      integrationID: "86ce9fb6-2ca4-48ec-aeb3-ddbed260132b", // The ID of this integration.
      region: "us-south", // The region your integration is hosted in.
      serviceInstanceID: "77eeeda2-2b53-4a2e-bfcd-3b68cd38e464", // The ID of your service instance.
      onLoad: function (instance) { instance.render(); }
    };
    setTimeout(function () {
      const t = document.createElement('script');
      t.src = "https://web-chat.global.assistant.watson.appdomain.cloud/versions/" + (window.watsonAssistantChatOptions.clientVersion || 'latest') + "/WatsonAssistantChatEntry.js";
      document.head.appendChild(t);
    });
  </script>
  <style>
    body {
      background: rgb(255, 255, 255);
      height: 553px;
      text-align: center;
      font-family: cursive;
    }

    h3 {
      color: rgb(6, 241, 238);
      font-size: 40px;
    }

    .normal
    {
      border: 2px;
      border-style: groove;
      border-radius: 7px;
      padding-top: 8px;
      padding-left: 8px;
      padding-bottom: 8px;
      padding-right: 8px;
      border-color: rgb(0, 0, 0);
      height: 25px;
      width: 400px;
    }

    button {
      border: 2px;
      border-radius: 10px;
      padding-top: 8px;
      padding-left: 8px;
      padding-bottom: 8px;
      padding-right: 8px;
      border-style: groove;
      width: 90px;
      opacity: 90%;
      border-color: rgb(0, 0, 0);
      cursor: pointer;
    }

    .right {
      width: 50%;
      float: right;
    }

    .left {
      width: 50%;
      float: left;
    }

    p {
    text-align: left;
    padding-left: 7px;
}

    .address {
      border: 2px;
      border-style: groove;
      border-radius: 7px;
      padding-top: 8px;
      padding-left: 8px;
      padding-bottom: 8px;
      padding-right: 8px;
      border-color: rgb(0, 0, 0);
      height: 95px;
      width: 395px;
    }

    .req_cont {
    margin-top: 50px;
    width: 40%;
    border: 1px solid #9c9c9c;
    border-radius: 9px;
    box-shadow: 4px 3px 11px 0px grey;
    background-color: #ff4848;
}
    .req_cont_main {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }

    .bottom_py {
      width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;

    }
    .form{
     display:flex;
     flex-direction: column;
     align-items: center;
     justify-content:center;
    }
  </style>
</head>

<body>
  <div class="req_cont_main">
    <div class="req_cont">

        <h3>APPLY FOR PLASMA DONATION</h3>
        <form method="post" class="form">


          <input class="normal" type="text" name="name" placeholder="Name" required /><br>
          <input class="normal" type="email" name="email" placeholder="Email" required /><br>
          <input class="normal" type="number" name="mobile" placeholder="Mobile" required /><br>
          <input class="normal" type="number" name="age" placeholder="Age" required /><br>
          <input class="normal" type="text" name="sex" placeholder="Gender" required /><br>



          <input class="normal" type="text" name="blood_group" placeholder="Blood Group" required /><br>
       
          <textarea class="address" name="address" placeholder="Address" required ></textarea><br>
  
          <input class="normal" type="text" name="covid" placeholder="Date tested covid positive in this format yyyy-mm-dd" required /><br>


          <button style="text-align: center;" type="submit">Request</button>
        </form>
        <div class="bottom_py">
          <p style="color: rgb(27, 161, 27);">{{success}}</p>
          <p style="color: rgb(214, 25, 25);">{{error}}</p>
        </div>
 
    </div>
  </div>
</body>

</html>