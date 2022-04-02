require 'httparty'

class Request
    include HTTParty
    
    def ping(url)
        HTTParty.get(url).code
    end
end

requests = Request.new()

(1..3).each do |n| # change 3 to whatever length you want
    [*'a'..'z', *0..9].combination(n).each do |c|
        s = c.join
        if s.length == 3 # change 3 to what you put in above "(1..X).each"
            if requests.ping("https://api.mojang.com/users/profiles/minecraft/" + s) == 204
                puts "[+] FOUND: " + s
            end
        end
    end
end
