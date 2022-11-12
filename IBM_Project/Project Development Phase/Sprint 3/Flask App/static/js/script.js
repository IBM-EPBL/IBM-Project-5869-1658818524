// import Chart from 'chart.js/auto';
d = [0,0,0,0,0,0,0,0,0,0]
var myChart        = null; 
var result_number = document.getElementById('result-digit');
var result = document.getElementById('result1');
var img_c = document.getElementById('image1')

function updateImage(event)
{
  img_c.style.display = 'block';
  var img = document.getElementById('img1');
  img.src = URL.createObjectURL(event.target.files[0])
  img.onload = function(){
    URL.revokeObjectURL(img.src)
  }

}

function Chart1(d) {
  try
  {
      var chart1 = document.getElementById('myChart1');
      if(myChart)
      {
        myChart.destroy();
        document.querySelector("#chart-div1").innerHTML = '<canvas id = "myChart1"></canvas>';
        chart1 = document.getElementById('myChart1');
        console.log('1')
      }
    }
    catch
    {
      console.log("Error")
    }
    const labels = [
        '0',
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9'
      ];
      const data = {
        labels: labels,
        datasets: [{
          label: 'Recognised Digit',
          backgroundColor: 'rgb(0, 128, 255)',
          borderColor: 'rgb(255, 99, 132)',
          data: d,
        }]
      };
    
      const config = {
        type: 'bar',
        data: data,
        options: {}
      };
    myChart = new Chart(
        chart1,
        config
      )
    

}

async function predict() {
    url = "http://localhost:5000/predict"
    const formData = new FormData();
    const files = document.getElementById("myfile");
    formData.append("file", files.files[0]);
    const requestOptions = {
        headers: {
            "Content-Type": files.files[0].contentType,
        },
            mode: "no-cors",
            method: "POST",
            files: files.files[0],
            body: formData,
        };
        
    try{
        const response = await fetch(url,requestOptions);
        

        if (response) {
            var data = await response.json();
            var ans = data[1]
            d = [0,0,0,0,0,0,0,0,0,0]
            d[ans] = 100;
            result.style.display = 'block';
            result_number.innerText = ans;

            Chart1(d);
            

        }
    }
    catch(error) {
        console.log(error);
    }
}
