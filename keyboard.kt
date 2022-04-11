// ==== KEYBOARD FILE ====
// Keyboard.kt
import java.awt.Robot

var r: Robot? = null

// Returns 0 if failed
// Returns 1 if success
@Throws(InterruptedException::class)
public fun pressKey(key: Int, delay: Double): Int {
    return try {
        r?.keyPress(key) // Presses key
        Thread.sleep(delay.toLong()) // Sleeps
        r?.keyRelease(key) // Releases key
        1 // Returns 1
    } catch (e: Exception) {
        0 // Returns 0
    }
}



// ==== MAIN FILE ====
// Main.kt
import java.awt.event.KeyEvent

class Main {
    fun main() {
        pressKey(KeyEvent.VK_W, 0.1)
    }
}
