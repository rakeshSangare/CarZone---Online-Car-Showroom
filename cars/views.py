from django.shortcuts import render, get_object_or_404  # Import render for rendering templates, get_object_or_404 for retrieving objects or returning a 404 error if not found
from cars.models import Car  # Import the Car model from the cars app
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator  # Import pagination classes for handling pagination

# View to display all cars with pagination
def cars(request):
    # Retrieve all car objects, ordered by creation date in descending order
    cars = Car.objects.order_by('-created_date')
    
    # Retrieve distinct values for model, city, year, and body style for search filters
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()

    # Set up pagination, showing 4 cars per page
    paginator = Paginator(cars, 4)
    page = request.GET.get('page')  # Get the current page number from the request
    paged_cars = paginator.get_page(page)  # Get the cars for the current page

    # Context data to be passed to the template
    data = {
        "cars": paged_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    
    # Render the cars.html template with the context data
    return render(request, 'cars/cars.html', data)

# View to display details of a single car
def car_detail(request, id):
    # Retrieve a single car by its primary key (id) or return a 404 error if not found
    single_car = get_object_or_404(Car, pk=id)

    # Context data to be passed to the template
    data = {
        "single_car": single_car,
    }

    # Render the car_detail.html template with the context data
    return render(request, 'cars/car_detail.html', data)

# View to handle car search functionality
def search(request):
    # Retrieve all car objects
    cars = Car.objects.all()
    
    # Retrieve distinct values for search filters
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct()

    # Keyword search
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)
    
    # Model filter
    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)
    
    # City filter
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city)
    
    # Year filter
    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)
    
    # Body style filter
    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)
    
    # Price range filter
    if 'min_price' in request.GET and 'max_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)
    
    # Transmission filter
    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission:
            cars = cars.filter(transmission__iexact=transmission)

    # Context data to be passed to the template
    data = {
        'cars': cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'transmission_search': transmission_search,
    }

    # Render the search.html template with the context data
    return render(request, 'cars/search.html', data)
