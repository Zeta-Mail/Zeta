{% extends "zeta/layout.html" %}
{% load static %}

{% block body %}


<?php

    $message_sent = false;

    if(isset($_POST['name']) && isset($_POST['email']) && isset($_POST['message']) && $_POST['name'] != '' && $_POST['email'] != '' && $_POST['message'] != ''){

        if(filter_var ($_POST['email'], FILTER_VALIDATE_EMAIL)){
            //Submit the form 

            $userName = $_POST['name'];
            $userEmail = $_POST['email'];
            $userMessage = $_POST['message'];

            $to = "nisini.20191213@iit.ac.lk";
            $subject = "Response from Zeta Mail Contact form";
            $body = "You have recieved the following feedback from Zeta Mail contact form. \r\n\r\n";

            $body .="From : ".$userName. "\r\n";
            $body .="Email Address : ".$userEmail. "\r\n";
            $body .="The Feedback/Suggestion : ".$userMessage. "\r\n";

            mail($to, $subject, $body);

            $message_sent = true;

        }
        
    }

?>
  
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    *{
	margin:0;
	padding:0;
	box-sizing: border-box;
	font-family: 'Poppins', sans-serif;
}

.subContainer{
	box-sizing: border-box;
	width: 100%;
}

.contact{
	position:relative;
	min-height: 100vh;
	padding :50px 100px;
	display: flex;
	justify-content: center;
	align-items: center;
	flex-direction: column;
	background: url(bg.jpg);
	background-size: cover;
}

.contact .content{
	max-width: 800px;
	text-align: center;
}

.contact .content h2{
	font-size :36px;
	font-weight:500;
	color: #fff;
}

.contact .content p{
	font-weight:300;
	color: #fff;
}

.container{
	width: 100%;
	display:flex;
	justify-content: center;
	align-items: center;
	margin-top:30px;
}

.container .contactInfo {
	width: 50%;
	display: flex;
	flex-direction: column;
}

.container .contactInfo .box{
	position: relative;
	padding: 20px 0;
	display: flex;
	margin-left:-10px;
	
}

.container .contactInfo .box .icon{
	min-width: 60px;
	height: 60px;
	background: #003A3A;
	display:flex;
	justify-content: center;
	align-items: center;
	border-radius: 50%;
	font-size: 22px;
}

.container .contactInfo .box .icon i{
	color: #fff;
	font-size: 28px;
}


.container .contactInfo .box .text{
	display: flex;
	margin-left:20px;
	font-size :14px;
	color: #fff;
	flex-direction:column;
	font-weight: 300;
}

.container .contactInfo .box .text h3{
	color: #003A3A;
	font-weight: 500;
}

.contactForm{
	width: 40%;
	padding: 40px;
	background: #fff;
	border-radius:5%;
}

.contactForm h2{
	font-size: 30px;
	color: #003A3A;
	font-weight: 500;
}

.contactForm .inputBox{
	width: 100%;
	position: relative;
	margin-top: 10px;
}

.contactForm .inputBox input,
.contactForm .inputBox textarea{
	width: 100%;
	padding: 5px 0;
	font-size: 16px;
	margin: 15px 0;
	border: none;
	border-bottom: 2px solid #003A3A;
	outline: none;
	resize:none;
}

.contactForm .inputBox span{
	position: absolute;
	left: 0;
	padding: 5px 0;
	font-size: 16px;
	margin: 15px 0;
	pointer-events: none;
	transition: 0.5s;
	color: #003A3A;
}

.contactForm .inputBox input:focus ~ span,
.contactForm .inputBox input:valid ~ span,
.contactForm .inputBox textarea:focus ~ span,
.contactForm .inputBox textarea:valid ~ span{
	color: teal;
	font-size: 12px;
	transform: translateY(-20px);
}

.contactForm .inputBox input[type="submit"]{
	width: 100px;
	background: teal;
	color:#fff;
	border-radius: 5%;
	border:none;
	cursor:pointer;
	padding:10px;
	font-size: 18px;
}

.contactForm .inputBox button{
	width: 300px;
	background: teal;
	color:#fff;
	border-radius: 5%;
	border:none;
	cursor:pointer;
	padding:10px;
	font-size: 18px;
	margin-top:20%;
}

.contactForm .inputBox button a{
	text-decoration: none;
	color:#fff;
}

.contactForm .inputBox input[type="submit"]:hover{
	background: #003A3A;
}

.contactForm .inputBox button:hover{
	background: #003A3A;
}

@media (max-width :991px){

	.contact{
		padding:50px;
	}
	
	.container{
		flex-direction:column;
	}
	
	.container .contactInfo{
		margin-bottom: 40px;
	}
	
	.container .contactInfo,
	.contactForm{
		width: 100%;
	}
}

</style>


<body>
	<div class="subContainer">
		<section class ="contact">
			<div class = "content">
				<h2>Contact Us</h2>
				<p>Have Questions, Feedback or Suggestions? Don't hesitate to contact us.
				We'd love it hear it, but please don't share any sensitive information.</p>		
			</div>
			
			<div class = "container">
				<div class = "contactInfo">
					<div class = "box">
						<div class = "icon"><i class='bx bx-mail-send'></i></i></div>
						<div class = "text">
							<h1>Email Address</h1>
							<p>nisiniweerathunga1814@gmail.com
							<br>sachinimalsha20@gmail.com
							<br>nadundias321@gmail.com</p>
						</div>
					</div>
					
					<div class = "box">
						<div class = "icon"><i class='bx bx-phone'></i></div>
						<div class = "text">
							<h1>Mobile Number</h1>
							<p>+94-76-893-2542
							<br>+94-77-560-5299</p>
						</div>
					</div>
					
				</div>

                <?php
                if($message_sent):
                ?>

                    <div class = "contactForm">
                        <h2>Thank you for the Feedback!</h2><br>
                        <h2>We'll be in touch...</h2>

                        <form>
                            <div class="inputBox">
                                <button><a href="ContactPage.php">Send Another Response</a></button>
                            </div>
                        </form>
                    </div>

                <?php
                else:
                ?>

                    <div class = "contactForm">
                        <form action="ContactPage.php" method="POST">
                            <h2>Send Message</h2>
                            <div class="inputBox">
                                <input type="text" name="name" required="required">
                                <span>Full Name</span>
                            </div>
                            <div class="inputBox">
                                <input type="email" name="email" required="required">
                                <span>Email Address</span>
                            </div>
                            <div class="inputBox">
                                <textarea required="required" name="message"></textarea>
                                <span>Type Your Message...</span>
                            </div>
                            <div class="inputBox">
                                <input type="submit" value="Send">
                            </div>
                        </form>
                    </div>

                <?php
                endif;
                ?>


				
			</div>
		</section>

	</div>
		
	<script>
    </script>
</body>
</html>

{% endblock %}