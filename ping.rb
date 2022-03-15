require 'httparty'

# Method 1
puts "--- Method 1 ---"
class Ping
    include HTTParty

    def initialize
    end
    
    def ping
        HTTParty.get('https://terrifictable.xyz').code
    end
end

p = Ping.new()
puts p.ping


# Method 2
puts "\n--- Method 2 ---"
puts HTTParty.get('https://terrifictable.xyz').code
