from PIL import Image, ImageDraw, ImageFont
from math import sin, cos, pi, radians, sqrt

class BIOImage:
    def __init__(self, Tsize, color):
        self.img = Image.new('RGBA', Tsize, color)

    def drawNum(self, Tpos, name, size):
        image = Image.new('RGBA', (60, 60))
        draw = ImageDraw.Draw(image)

        draw.ellipse((0, 0, 60, 60), fill='black')
        draw.ellipse((7, 7, 53, 53), fill='white')
        f = ImageFont.truetype('arial.ttf', 20)
        draw.text((16, 16), name, font=f, fill='black')

        image = image.resize((size, size), Image.ANTIALIAS)
        self.img.paste(image, [item - int(size / 2) for item in Tpos], image)

    def drawNodeC(self, Tpos, name, size):
        image = Image.new('RGBA', (60, 60))
        draw = ImageDraw.Draw(image)

        draw.ellipse((0, 0, 60, 60), fill='black')
        draw.ellipse((7, 7, 53, 53), fill='white')
        f = ImageFont.truetype('arial.ttf', 40)
        draw.text((15, 9), name, font=f, fill='black')

        image = image.resize((size, size), Image.ANTIALIAS)
        self.img.paste(image, [item - int(size / 2) for item in Tpos], image)

    def drawNodeG(self, Tpos, name, size):
        image = Image.new('RGBA', (60, 60))
        draw = ImageDraw.Draw(image)

        draw.ellipse((0, 0, 60, 60), fill='black')
        draw.ellipse((7, 7, 53, 53), fill='white')
        f = ImageFont.truetype('arial.ttf', 40)
        draw.text((15, 9), name, font=f, fill='black')

        image = image.resize((size, size), Image.ANTIALIAS)
        self.img.paste(image, [item - int(size / 2) for item in Tpos], image)

    def drawNodeA(self, Tpos, name, size):
        image = Image.new('RGBA', (60, 60))
        draw = ImageDraw.Draw(image)

        draw.ellipse((0, 0, 60, 60), fill='black')
        draw.ellipse((7, 7, 53, 53), fill='white')
        f = ImageFont.truetype('arial.ttf', 40)
        draw.text((17, 7), name, font=f, fill='black')

        image = image.resize((size, size), Image.ANTIALIAS)
        self.img.paste(image, [item - int(size / 2) for item in Tpos], image)

    def drawNodeU(self, Tpos, name, size):
        image = Image.new('RGBA', (60, 60))
        draw = ImageDraw.Draw(image)

        draw.ellipse((0, 0, 60, 60), fill='black')
        draw.ellipse((7, 7, 53, 53), fill='white')
        f = ImageFont.truetype('arial.ttf', 40)
        draw.text((16, 10), name, font=f, fill='black')

        image = image.resize((size, size), Image.ANTIALIAS)
        self.img.paste(image, [item - int(size / 2) for item in Tpos], image)

    def drawCircleLine(self, Tfrom, Tto):
        draw = ImageDraw.Draw(self.img)
        draw.line(Tfrom + Tto, fill='black', width=7)

    def drawWWcis(self, Tfrom, Tto, size):
        def drawWWline(self, Tfrom, Tto):
            draw = ImageDraw.Draw(self.img)
            draw.line(Tfrom + Tto, fill='red', width=8)

        def drawWWcircle(self, size):
            sx = ((Tto[0] + Tfrom[0]) / 2)
            sy = ((Tto[1] + Tfrom[1]) / 2)

            Tpos = (int(sx), int(sy))
            image = Image.new('RGBA', (60, 60))

            draw = ImageDraw.Draw(image)
            draw.ellipse((0, 0, 60, 60), fill='red')
            image = image.resize((size, size), Image.ANTIALIAS)
            self.img.paste(image, [item - int(size / 2) for item in Tpos], image)

        drawWWline(self, Tfrom, Tto)
        drawWWcircle(self, size)

    def drawWWtrans(self, Tfrom, Tto, size):
        def drawWWline(self, Tfrom, Tto):
            draw = ImageDraw.Draw(self.img)
            draw.line(Tfrom + Tto, fill='red', width=8)

        def drawWWcircle(self, size):
            sx = ((Tto[0] + Tfrom[0]) / 2)
            sy = ((Tto[1] + Tfrom[1]) / 2)

            Tpos = (int(sx), int(sy))
            image = Image.new('RGBA', (60, 60))

            draw = ImageDraw.Draw(image)
            draw.ellipse((0, 0, 60, 60), fill='red')
            draw.ellipse((7, 7, 53, 53), fill='white')
            image = image.resize((size, size), Image.ANTIALIAS)
            self.img.paste(image, [item - int(size / 2) for item in Tpos], image)

        drawWWline(self, Tfrom, Tto)
        drawWWcircle(self, size)

    def drawWHcis(self, Tfrom, Tto, size):
        def drawWHline(self, Tfrom, Tto):
            draw = ImageDraw.Draw(self.img)
            draw.line(Tfrom + Tto, fill='red', width=8)

        def drawWHcircle(self, size):
            sx = ((Tto[0] + Tfrom[0]) / 2)
            sy = ((Tto[1] + Tfrom[1]) / 2)

            Tpos = (int(sx), int(sy))
            image = Image.new('RGBA', (60, 60))

            draw = ImageDraw.Draw(image)
            draw.ellipse((0, 0, 60, 60), fill='red')
            image = image.resize((size, size), Image.ANTIALIAS)
            self.img.paste(image, [item - int(size / 2) for item in Tpos], image)

        def drawWHsquare(self, Tfrom, size):
            draw = ImageDraw.Draw(self.img)

            sx = ((9 * Tto[0] + 7 * Tfrom[0]) / 16)
            sy = ((9 * Tto[1] + 7 * Tfrom[1]) / 16)

            vx = Tto[0] - Tfrom[0]
            vy = Tto[1] - Tfrom[1]

            x1 = sx + vy / sqrt(vx ** 2 + vy ** 2) * size
            y1 = sy - vx / sqrt(vx ** 2 + vy ** 2) * size

            x2 = sx - vy / sqrt(vx ** 2 + vy ** 2) * size
            y2 = sy + vx / sqrt(vx ** 2 + vy ** 2) * size

            x3 = x1 - 2 * vx / sqrt(vx ** 2 + vy ** 2) * size
            y3 = y1 - 2 * vy / sqrt(vx ** 2 + vy ** 2) * size

            x4 = x2 - 2 * vx / sqrt(vx ** 2 + vy ** 2) * size
            y4 = y2 - 2 * vy / sqrt(vx ** 2 + vy ** 2) * size

            draw.polygon(((x1, y1), (x2, y2), (x4, y4), (x3, y3)), fill="red")

        drawWHline(self, Tfrom, Tto)
        drawWHcircle(self, size)
        drawWHsquare(self, Tfrom, size)

    def drawWHtrans(self, Tfrom, Tto, size):
        def drawWHline(self, Tfrom, Tto):
            draw = ImageDraw.Draw(self.img)
            draw.line(Tfrom + Tto, fill='red', width=8)

        def drawWHcircle(self, size):
            sx = ((Tto[0] + Tfrom[0]) / 2)
            sy = ((Tto[1] + Tfrom[1]) / 2)

            Tpos = (int(sx), int(sy))
            image = Image.new('RGBA', (60, 60))

            draw = ImageDraw.Draw(image)
            draw.ellipse((0, 0, 60, 60), fill='red')
            draw.ellipse((7, 7, 53, 53), fill='white')
            image = image.resize((size, size), Image.ANTIALIAS)
            self.img.paste(image, [item - int(size / 2) for item in Tpos], image)

        def drawWHsquare(self, Tfrom, size):
            draw = ImageDraw.Draw(self.img)

            sx = ((9 * Tto[0] + 7 * Tfrom[0]) / 16)
            sy = ((9 * Tto[1] + 7 * Tfrom[1]) / 16)

            vx = Tto[0] - Tfrom[0]
            vy = Tto[1] - Tfrom[1]

            x1 = sx + vy / sqrt(vx ** 2 + vy ** 2) * size
            y1 = sy - vx / sqrt(vx ** 2 + vy ** 2) * size

            x2 = sx - vy / sqrt(vx ** 2 + vy ** 2) * size
            y2 = sy + vx / sqrt(vx ** 2 + vy ** 2) * size

            x3 = x1 - 2 * vx / sqrt(vx ** 2 + vy ** 2) * size
            y3 = y1 - 2 * vy / sqrt(vx ** 2 + vy ** 2) * size

            x4 = x2 - 2 * vx / sqrt(vx ** 2 + vy ** 2) * size
            y4 = y2 - 2 * vy / sqrt(vx ** 2 + vy ** 2) * size

            draw.polygon(((x1, y1), (x2, y2), (x4, y4), (x3, y3)), fill="white", outline="red")

        drawWHline(self, Tfrom, Tto)
        drawWHcircle(self, size)
        drawWHsquare(self, Tfrom, size)

    def drawWScis(self, Tfrom, Tto, size):
        def drawWSline(self, Tfrom, Tto):
            draw = ImageDraw.Draw(self.img)
            draw.line(Tfrom + Tto, fill='red', width=8)

        def drawWScircle(self, size):
            sx = ((Tto[0] + Tfrom[0]) / 2)
            sy = ((Tto[1] + Tfrom[1]) / 2)

            Tpos = (int(sx), int(sy))
            image = Image.new('RGBA', (60, 60))

            draw = ImageDraw.Draw(image)
            draw.ellipse((0, 0, 60, 60), fill='red')
            image = image.resize((size, size), Image.ANTIALIAS)
            self.img.paste(image, [item - int(size / 2) for item in Tpos], image)

        def drawWStriangle(self, Tfrom, size):
            draw = ImageDraw.Draw(self.img)

            x1 = ((11 * Tto[0] + 9 * Tfrom[0]) / 20) + size * ((Tfrom[1] - Tto[1])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))
            y1 = ((11 * Tto[1] + 9 * Tfrom[1]) / 20) + size * ((Tto[0] - Tfrom[0])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))

            x2 = ((11 * Tto[0] + 9 * Tfrom[0]) / 20) - size * ((Tfrom[1] - Tto[1])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))
            y2 = ((11 * Tto[1] + 9 * Tfrom[1]) / 20) - size * ((Tto[0] - Tfrom[0])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))

            x3 = ((11 * Tto[0] + 9 * Tfrom[0]) / 20) + 2 * size * (Tto[0] - Tfrom[0]) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))
            y3 = ((11 * Tto[1] + 9 * Tfrom[1]) / 20) + 2 * size * (Tto[1] - Tfrom[1]) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))

            draw.polygon(((x1, y1), (x2, y2), (x3, y3)), fill="red")

        drawWSline(self, Tfrom, Tto)
        drawWStriangle(self, Tfrom, size)
        drawWScircle(self, size)

    def drawWStrans(self, Tfrom, Tto, size):
        def drawWSline(self, Tfrom, Tto):
            draw = ImageDraw.Draw(self.img)
            draw.line(Tfrom + Tto, fill='red', width=8)

        def drawWScircle(self, size):
            sx = ((Tto[0] + Tfrom[0]) / 2)
            sy = ((Tto[1] + Tfrom[1]) / 2)

            Tpos = (int(sx), int(sy))
            image = Image.new('RGBA', (60, 60))

            draw = ImageDraw.Draw(image)
            draw.ellipse((0, 0, 60, 60), fill='red')
            draw.ellipse((7, 7, 53, 53), fill='white')
            image = image.resize((size, size), Image.ANTIALIAS)
            self.img.paste(image, [item - int(size / 2) for item in Tpos], image)

        def drawWStriangle(self, Tfrom, size):
            draw = ImageDraw.Draw(self.img)

            x1 = ((11 * Tto[0] + 9 * Tfrom[0]) / 20) + size * ((Tfrom[1] - Tto[1])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))
            y1 = ((11 * Tto[1] + 9 * Tfrom[1]) / 20) + size * ((Tto[0] - Tfrom[0])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))

            x2 = ((11 * Tto[0] + 9 * Tfrom[0]) / 20) - size * ((Tfrom[1] - Tto[1])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))
            y2 = ((11 * Tto[1] + 9 * Tfrom[1]) / 20) - size * ((Tto[0] - Tfrom[0])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))

            x3 = ((11 * Tto[0] + 9 * Tfrom[0]) / 20) + 2 * size * (Tto[0] - Tfrom[0]) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))
            y3 = ((11 * Tto[1] + 9 * Tfrom[1]) / 20) + 2 * size * (Tto[1] - Tfrom[1]) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))

            size = size - 20

            t1 = ((11 * Tto[0] + 9 * Tfrom[0]) / 20) + size * ((Tfrom[1] - Tto[1])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))
            w1 = ((11 * Tto[1] + 9 * Tfrom[1]) / 20) + size * ((Tto[0] - Tfrom[0])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))

            t2 = ((11 * Tto[0] + 9 * Tfrom[0]) / 20) - size * ((Tfrom[1] - Tto[1])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))
            w2 = ((11 * Tto[1] + 9 * Tfrom[1]) / 20) - size * ((Tto[0] - Tfrom[0])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))

            t3 = ((11 * Tto[0] + 9 * Tfrom[0]) / 20) + 2 * size * (Tto[0] - Tfrom[0]) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))
            w3 = ((11 * Tto[1] + 9 * Tfrom[1]) / 20) + 2 * size * (Tto[1] - Tfrom[1]) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))

            draw.polygon(((x1, y1), (x2, y2), (x3, y3)), fill="red")
            draw.polygon(((t1, w1), (t2, w2), (t3, w3)), fill="white", outline="red")

        drawWSline(self, Tfrom, Tto)
        drawWStriangle(self, Tfrom, size)
        drawWScircle(self, size)

    def drawHHcis(self, Tfrom, Tto, size):
        def drawHHline(self, Tfrom, Tto):
            draw = ImageDraw.Draw(self.img)
            draw.line(Tfrom + Tto, fill='red', width=8)

        def drawHHsquare(self, Tfrom, size):
            draw = ImageDraw.Draw(self.img)

            sx = ((9 * Tto[0] + 7 * Tfrom[0]) / 16)
            sy = ((9 * Tto[1] + 7 * Tfrom[1]) / 16)

            vx = Tto[0] - Tfrom[0]
            vy = Tto[1] - Tfrom[1]

            x1 = sx + vy / sqrt(vx ** 2 + vy ** 2) * size
            y1 = sy - vx / sqrt(vx ** 2 + vy ** 2) * size

            x2 = sx - vy / sqrt(vx ** 2 + vy ** 2) * size
            y2 = sy + vx / sqrt(vx ** 2 + vy ** 2) * size

            x3 = x1 - 2 * vx / sqrt(vx ** 2 + vy ** 2) * size
            y3 = y1 - 2 * vy / sqrt(vx ** 2 + vy ** 2) * size

            x4 = x2 - 2 * vx / sqrt(vx ** 2 + vy ** 2) * size
            y4 = y2 - 2 * vy / sqrt(vx ** 2 + vy ** 2) * size

            draw.polygon(((x1, y1), (x2, y2), (x4, y4), (x3, y3)), fill="red")

        drawHHline(self, Tfrom, Tto)
        drawHHsquare(self, Tfrom, size)

    def drawHHtrans(self, Tfrom, Tto, size):
        def drawHHline(self, Tfrom, Tto):
            draw = ImageDraw.Draw(self.img)
            draw.line(Tfrom + Tto, fill='red', width=8)

        def drawHHsquare(self, Tfrom, size):
            draw = ImageDraw.Draw(self.img)

            sx = ((9 * Tto[0] + 7 * Tfrom[0]) / 16)
            sy = ((9 * Tto[1] + 7 * Tfrom[1]) / 16)

            vx = Tto[0] - Tfrom[0]
            vy = Tto[1] - Tfrom[1]

            x1 = sx + vy / sqrt(vx ** 2 + vy ** 2) * size
            y1 = sy - vx / sqrt(vx ** 2 + vy ** 2) * size

            x2 = sx - vy / sqrt(vx ** 2 + vy ** 2) * size
            y2 = sy + vx / sqrt(vx ** 2 + vy ** 2) * size

            x3 = x1 - 2 * vx / sqrt(vx ** 2 + vy ** 2) * size
            y3 = y1 - 2 * vy / sqrt(vx ** 2 + vy ** 2) * size

            x4 = x2 - 2 * vx / sqrt(vx ** 2 + vy ** 2) * size
            y4 = y2 - 2 * vy / sqrt(vx ** 2 + vy ** 2) * size

            draw.polygon(((x1, y1), (x2, y2), (x4, y4), (x3, y3)), fill="white", outline="red")

        drawHHline(self, Tfrom, Tto)
        drawHHsquare(self, Tfrom, size)

    def drawHScis(self, Tfrom, Tto, size):
        def drawHSline(self, Tfrom, Tto):
            draw = ImageDraw.Draw(self.img)
            draw.line(Tfrom + Tto, fill='red', width=8)

        def drawHStriangle(self, Tfrom, size):
            draw = ImageDraw.Draw(self.img)

            x1 = ((9 * Tto[0] + 7 * Tfrom[0]) / 16) + size * ((Tfrom[1] - Tto[1])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))
            y1 = ((9 * Tto[1] + 7 * Tfrom[1]) / 16) + size * ((Tto[0] - Tfrom[0])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))

            x2 = ((9 * Tto[0] + 7 * Tfrom[0]) / 16) - size * ((Tfrom[1] - Tto[1])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))
            y2 = ((9 * Tto[1] + 7 * Tfrom[1]) / 16) - size * ((Tto[0] - Tfrom[0])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))

            x3 = ((9 * Tto[0] + 7 * Tfrom[0]) / 16) + 2 * size * (Tto[0] - Tfrom[0]) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))
            y3 = ((9 * Tto[1] + 7 * Tfrom[1]) / 16) + 2 * size * (Tto[1] - Tfrom[1]) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))

            draw.polygon(((x1, y1), (x2, y2), (x3, y3)), fill="red")

        def drawHSsquare(self, Tfrom, size):
            draw = ImageDraw.Draw(self.img)

            sx = ((Tto[0] + Tfrom[0]) / 2)
            sy = ((Tto[1] + Tfrom[1]) / 2)

            vx = Tto[0] - Tfrom[0]
            vy = Tto[1] - Tfrom[1]

            x1 = sx + vy / sqrt(vx ** 2 + vy ** 2) * size
            y1 = sy - vx / sqrt(vx ** 2 + vy ** 2) * size

            x2 = sx - vy / sqrt(vx ** 2 + vy ** 2) * size
            y2 = sy + vx / sqrt(vx ** 2 + vy ** 2) * size

            x3 = x1 - 2 * vx / sqrt(vx ** 2 + vy ** 2) * size
            y3 = y1 - 2 * vy / sqrt(vx ** 2 + vy ** 2) * size

            x4 = x2 - 2 * vx / sqrt(vx ** 2 + vy ** 2) * size
            y4 = y2 - 2 * vy / sqrt(vx ** 2 + vy ** 2) * size

            draw.polygon(((x1, y1), (x2, y2), (x4, y4), (x3, y3)), fill="red")

        drawHSline(self, Tfrom, Tto)
        drawHStriangle(self, Tfrom, size)
        drawHSsquare(self, Tfrom, size)

    def drawHStrans(self, Tfrom, Tto, size):
        def drawHSline(self, Tfrom, Tto):
            draw = ImageDraw.Draw(self.img)
            draw.line(Tfrom + Tto, fill='red', width=8)

        def drawHStriangle(self, Tfrom, size):
            draw = ImageDraw.Draw(self.img)

            x1 = ((9 * Tto[0] + 7 * Tfrom[0]) / 16) + size * ((Tfrom[1] - Tto[1])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))
            y1 = ((9 * Tto[1] + 7 * Tfrom[1]) / 16) + size * ((Tto[0] - Tfrom[0])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))

            x2 = ((9 * Tto[0] + 7 * Tfrom[0]) / 16) - size * ((Tfrom[1] - Tto[1])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))
            y2 = ((9 * Tto[1] + 7 * Tfrom[1]) / 16) - size * ((Tto[0] - Tfrom[0])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))

            x3 = ((9 * Tto[0] + 7 * Tfrom[0]) / 16) + 2 * size * (Tto[0] - Tfrom[0]) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))
            y3 = ((9 * Tto[1] + 7 * Tfrom[1]) / 16) + 2 * size * (Tto[1] - Tfrom[1]) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))

            size = size - 20

            t1 = ((9 * Tto[0] + 7 * Tfrom[0]) / 16) + size * ((Tfrom[1] - Tto[1])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))
            w1 = ((9 * Tto[1] + 7 * Tfrom[1]) / 16) + size * ((Tto[0] - Tfrom[0])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))

            t2 = ((9 * Tto[0] + 7 * Tfrom[0]) / 16) - size * ((Tfrom[1] - Tto[1])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))
            w2 = ((9 * Tto[1] + 7 * Tfrom[1]) / 16) - size * ((Tto[0] - Tfrom[0])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))

            t3 = ((9 * Tto[0] + 7 * Tfrom[0]) / 16) + 2 * size * (Tto[0] - Tfrom[0]) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))
            w3 = ((9 * Tto[1] + 7 * Tfrom[1]) / 16) + 2 * size * (Tto[1] - Tfrom[1]) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))

            draw.polygon(((x1, y1), (x2, y2), (x3, y3)), fill="red")
            draw.polygon(((t1, w1), (t2, w2), (t3, w3)), fill="white", outline="red")

        def drawHSsquare(self, Tfrom, size):
            draw = ImageDraw.Draw(self.img)

            sx = ((Tto[0] + Tfrom[0]) / 2)
            sy = ((Tto[1] + Tfrom[1]) / 2)

            vx = Tto[0] - Tfrom[0]
            vy = Tto[1] - Tfrom[1]

            x1 = sx + vy / sqrt(vx ** 2 + vy ** 2) * size
            y1 = sy - vx / sqrt(vx ** 2 + vy ** 2) * size

            x2 = sx - vy / sqrt(vx ** 2 + vy ** 2) * size
            y2 = sy + vx / sqrt(vx ** 2 + vy ** 2) * size

            x3 = x1 - 2 * vx / sqrt(vx ** 2 + vy ** 2) * size
            y3 = y1 - 2 * vy / sqrt(vx ** 2 + vy ** 2) * size

            x4 = x2 - 2 * vx / sqrt(vx ** 2 + vy ** 2) * size
            y4 = y2 - 2 * vy / sqrt(vx ** 2 + vy ** 2) * size

            draw.polygon(((x1, y1), (x2, y2), (x4, y4), (x3, y3)), fill="white", outline="red")

        drawHSline(self, Tfrom, Tto)
        drawHStriangle(self, Tfrom, size)
        drawHSsquare(self, Tfrom, size)

    def drawSScis(self, Tfrom, Tto, size):
        def drawSSline(self, Tfrom, Tto):
            draw = ImageDraw.Draw(self.img)
            draw.line(Tfrom + Tto, fill='red', width=8)

        def drawSStriangle(self, Tfrom, size):
            draw = ImageDraw.Draw(self.img)

            x1 = ((Tto[0] + Tfrom[0]) / 2) + size * ((Tfrom[1] - Tto[1])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))
            y1 = ((Tto[1] + Tfrom[1]) / 2) + size * ((Tto[0] - Tfrom[0])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))

            x2 = ((Tto[0] + Tfrom[0]) / 2) - size * ((Tfrom[1] - Tto[1])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))
            y2 = ((Tto[1] + Tfrom[1]) / 2) - size * ((Tto[0] - Tfrom[0])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))

            x3 = ((Tto[0] + Tfrom[0]) / 2) + 2 * size * (Tto[0] - Tfrom[0]) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))
            y3 = ((Tto[1] + Tfrom[1]) / 2) + 2 * size * (Tto[1] - Tfrom[1]) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))

            draw.polygon(((x1, y1), (x2, y2), (x3, y3)), fill="red")

        drawSSline(self, Tfrom, Tto)
        drawSStriangle(self, Tfrom, size)

    def drawSStrans(self, Tfrom, Tto, size):
        def drawSSline(self, Tfrom, Tto):
            draw = ImageDraw.Draw(self.img)
            draw.line(Tfrom + Tto, fill='red', width=8)

        def drawSStriangle(self, Tfrom, size):
            draw = ImageDraw.Draw(self.img)

            x1 = ((Tto[0] + Tfrom[0]) / 2) + size * ((Tfrom[1] - Tto[1])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))
            y1 = ((Tto[1] + Tfrom[1]) / 2) + size * ((Tto[0] - Tfrom[0])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))

            x2 = ((Tto[0] + Tfrom[0]) / 2) - size * ((Tfrom[1] - Tto[1])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))
            y2 = ((Tto[1] + Tfrom[1]) / 2) - size * ((Tto[0] - Tfrom[0])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))

            x3 = ((Tto[0] + Tfrom[0]) / 2) + 2 * size * (Tto[0] - Tfrom[0]) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))
            y3 = ((Tto[1] + Tfrom[1]) / 2) + 2 * size * (Tto[1] - Tfrom[1]) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))

            size = size - 20

            t1 = ((Tto[0] + Tfrom[0]) / 2) + size * ((Tfrom[1] - Tto[1])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))
            w1 = ((Tto[1] + Tfrom[1]) / 2) + size * ((Tto[0] - Tfrom[0])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))

            t2 = ((Tto[0] + Tfrom[0]) / 2) - size * ((Tfrom[1] - Tto[1])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))
            w2 = ((Tto[1] + Tfrom[1]) / 2) - size * ((Tto[0] - Tfrom[0])) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))

            t3 = ((Tto[0] + Tfrom[0]) / 2) + 2 * size * (Tto[0] - Tfrom[0]) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))
            w3 = ((Tto[1] + Tfrom[1]) / 2) + 2 * size * (Tto[1] - Tfrom[1]) / (
                sqrt((Tfrom[1] - Tto[1]) ** 2 + (Tfrom[0] - Tto[0]) ** 2))

            draw.polygon(((x1, y1), (x2, y2), (x3, y3)), fill="red")
            draw.polygon(((t1, w1), (t2, w2), (t3, w3)), fill="white", outline="red")

        drawSSline(self, Tfrom, Tto)
        drawSStriangle(self, Tfrom, size)

    def show(self):
        self.img.show()

    def save(self, filename):
        self.img.save(filename)