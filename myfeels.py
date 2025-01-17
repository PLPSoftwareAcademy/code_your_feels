body{
    margin:0;
    padding:0;
    min-height:100vh;
    display: flex;
    justify-content: center;
    align-content: center;
    background:#0b1522;
}
/* love emoji */
.heart{
    height:350px;
    width:350px;
    background-color:red;
    position: relative;
    transform: rotate(45deg);
    box-shadow:-20px 20px 150px #f20044;
    padding-top:50;
    animation:palpitar 0.5s linear infinite alternate;
}
/* styling love message */
.content{
    position: fixed;
    margin-bottom:50px;
    text-align:center;
    font-style: italic;
}
@keyframes palpitar{
    0%{transform: rotate(45deg)scale(1.10);}
    80%{transform: rotate(45deg)scale(1.0);}
    100%{transform: rotate(45deg)scale(0.8);}
}
/* one circle on right */
.heart::before{
    content:"";
    position: absolute;
    height:350px;
    width:350px;
    background:red;
    right:50%;
    border-radius:50%;
    box-shadow:20px 20px 150px #f20044;
}
.heart::after{
    content:"";
    position: absolute;
    height:350px;
    width:350px;
    background:red;
    top:-50%;
    border-radius:50%;
    box-shadow:20px 20px 150px #f20044;
}
