const cityDataBox = document.getElementById('citys-data-box')
const cityInput = document.getElementById('citys')

const hotelDataBox = document.getElementById('hotel-data-box')
const hotelInput = document.getElementById('hotel')
const modelText = document.getElementById('hotel-text')


if(cityInput != null){
    $.ajax({
        type: 'GET',
        url: '/city-json/',
        success: function(response){
            console.log(response.data)
            const codesData = response.data
            codesData.map(item=>{
                const option = document.createElement('div')
                option.textContent = item.cityName
                option.setAttribute('class', 'item')
                option.setAttribute('data-value', item.cityCode)
                cityDataBox.appendChild(option)
            })
        },
        error: function(error){
            console.log(error)
        }
    })
    
    
    cityInput.addEventListener('change', e=>{
        console.log(e.target.value)
        const selectedcode = e.target.value
        
        hotelDataBox.innerHTML = ""
        modelText.textContent = "Choose a hotel"
        modelText.classList.add("default")
        
    
        $.ajax({
            type: 'GET',
            url: `/hotel-json/${selectedcode}/`,
            success: function(response){
                console.log(response.data)
                const hotelData = response.data
                hotelData.map(item=>{
                    const option = document.createElement('div')
                    option.textContent = item.hotelName
                    option.setAttribute('class', 'item')
                    option.setAttribute('data-value', item.hotelName)
                    hotelDataBox.appendChild(option)
                })
            },
            error: function(error){
                console.log(error)
            }
        })
        
    })
}
